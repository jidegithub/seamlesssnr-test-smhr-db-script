import subprocess
import argparse
import os
import gzip
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_database(db_name, backup_file):
    try:
        dump_command = [
            'mysqldump',
            f'--user={os.getenv("DB_USER")}',
            f'--password={os.getenv("DB_PASSWORD")}',
            f'--host={os.getenv("DB_HOST")}',
            db_name
        ]
        dump_output = subprocess.check_output(dump_command)
        
        with gzip.open(backup_file, 'wb') as f:
            f.write(dump_output)
        
        logging.info(f"Backup completed: {backup_file}")
    except subprocess.CalledProcessError as e:
        logging.error("Backup failed.")
        logging.exception(e)

def restore_database(db_name, backup_file):
    try:
        decompressed_dump = backup_file.replace('.gz', '_decompressed.sql')
        with gzip.open(backup_file, 'rb') as f_in, open(decompressed_dump, 'wb') as f_out:
            f_out.write(f_in.read())
        
        restore_command = [
            'mysql',
            f'--user={os.getenv("DB_USER")}',
            f'--password={os.getenv("DB_PASSWORD")}',
            f'--host={os.getenv("DB_HOST")}',
            db_name,
            f'< {decompressed_dump}'
        ]
        subprocess.run(' '.join(restore_command), shell=True, check=True)
        logging.info("Restoration completed.")
        
        os.remove(decompressed_dump)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        logging.error("Restoration failed.")
        logging.exception(e)

def main():
    parser = argparse.ArgumentParser(description="Automate database backup and restoration")
    parser.add_argument("operation", choices=["backup", "restore"], help="Choose 'backup' or 'restore' operation")
    parser.add_argument("db_name", help="Name of the database")
    parser.add_argument("backup_file", help="Path to backup file (use .gz extension for backup, .sql.gz)")
    
    args = parser.parse_args()

    setup_logging()

    if args.operation == "backup":
        backup_database(args.db_name, args.backup_file)
    elif args.operation == "restore":
        restore_database(args.db_name, args.backup_file)

if __name__ == "__main__":
    main()