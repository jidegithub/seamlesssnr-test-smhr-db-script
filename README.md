# Database Backup and Restoration Script

This Python script automates the process of backing up and restoring a database. It supports both backup and restore operations, provides error handling, and allows for customization of database parameters and backup file locations.

## Features

- Backup: Create a compressed dump of the specified database.
- Restore: Decompress a backup file and restore the database from the dump.
- Error Handling: Properly handle errors during backup and restoration processes.
- Configurable: Customize database credentials and backup locations through environment variables.
- Logging: Log important events and errors for troubleshooting.
- Command-line Interface: Use command-line arguments for specifying the operation, database name, and backup file.

## Prerequisites

- Python 3.5 or later
- MySQL client tools (`mysqldump` and `mysql`) installed
- `gzip` package for Python (install using `pip install gzip`)

## Usage

1. Clone or download the script to your local machine.

2. Install the required packages:

   ```bash
   pip install gzip
3. Set up environment variables for your database credentials
  ```python
    export DB_USER=your_database_username
    export DB_PASSWORD=your_database_password
    export DB_HOST=your_database_host
  ```

4. Run the script using the command-line interface:
    ```bash 
    python script.py [operation] [db_name] [backup_file]
    ```
[operation]: Choose between backup or restore.
[db_name]: Name of the database you want to backup or restore.
[backup_file]: Path to the backup file (use .gz extension for backup, .sql.gz)

5. Configuration
Modify the script to include the correct database credentials and host information in the backup_database and restore_database functions.


