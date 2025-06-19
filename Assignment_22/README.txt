================================================================================
           Duplicate File Cleaner and Email Notifier Automation Script
================================================================================

Author: Vrishabha  
Script Language: Python  
Dependencies: psutil, schedule, hashlib, smtplib, re, email, mimetypes, datetime  

--------------------------------------------------------------------------------
Overview:
--------------------------------------------------------------------------------

This Python script is designed to automate the task of scanning a given directory 
for duplicate files based on file content (using MD5 checksums), deleting those 
duplicates, logging the operation, and sending a report to your email.

The script runs at a user-defined time interval and handles everything 
automatically — making it ideal for periodic directory cleanups.

--------------------------------------------------------------------------------
Features:
--------------------------------------------------------------------------------

✔ Scans and detects duplicate files using checksum (MD5)  
✔ Deletes duplicate files while preserving the original  
✔ Logs all deleted files in a timestamped `.log` file  
✔ Sends the log file to your email with scan statistics  
✔ Schedule-based automation (every N minutes)  
✔ Command-line interface with usage/help flags  
✔ Email validation using regex  

--------------------------------------------------------------------------------
Log File:
--------------------------------------------------------------------------------

- Created inside the directory named `Marvellous/`
- Named format: `DeletedFiles_YYYYMMDD_HHMMSS.log`
- Contains:
    • List of deleted duplicate files
    • Total files scanned
    • Total files deleted
    • Timestamp of operation

--------------------------------------------------------------------------------
Statistics Included in the Email Body:
--------------------------------------------------------------------------------

- Start time of the scan  
- Total number of files scanned  
- Total number of duplicates found and deleted  

--------------------------------------------------------------------------------
How to Run:
--------------------------------------------------------------------------------

Usage:
    python ScriptName.py <DirectoryPath> <TimeIntervalInMinutes> <ReceiverEmail>

Example:
    python CleanDuplicates.py /Users/vrishabha/Downloads 10 vrishabha@example.com

Help:
    python ScriptName.py --h      : Display help
    python ScriptName.py --u      : Display usage instructions

--------------------------------------------------------------------------------
Dependencies Installation (if needed):
--------------------------------------------------------------------------------

    pip install psutil schedule

--------------------------------------------------------------------------------
Important Notes:
--------------------------------------------------------------------------------

- Provide a valid **absolute path** to the target directory.
- The script supports only **valid email addresses** using regex validation.
- The sender email is configured as: `demoforpython5@gmail.com`
- The email is sent via Gmail SMTP, so make sure:
    • The sender uses an app password.
    • You enable "Less Secure App Access" or use an app-specific password.

--------------------------------------------------------------------------------
Security Tip:
--------------------------------------------------------------------------------

Avoid hardcoding the email password in the script.  
Use environment variables or configuration files instead.

Example:
    import os
    password = os.getenv("EMAIL_PASSWORD")

Then run:
    EMAIL_PASSWORD=your_app_password python CleanDuplicates.py ...

--------------------------------------------------------------------------------
Thank You!
--------------------------------------------------------------------------------

This script was developed as part of a personal automation project.  
Feel free to enhance, reuse, or share it with proper attribution.

================================================================================
