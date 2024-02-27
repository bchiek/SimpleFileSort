# SimpleFileSort
 Python script that sorts files in a directory into subdirectories based on their file extensions.

## Requirements

Python 3.6 or later.

## Usage

Run the script and enter the directory you want to sort when prompted

## How It Works

The script prompts the user for a directory path. It then checks if the directory exists. If it does, the script gets a list of all files in the directory. For each file, it gets the file extension and creates a new directory for this file type (if it doesn't already exist). It then moves the file into the new directory.

![image](https://github.com/bchiek/SimpleFileSort/assets/99049187/8ec6ef1b-c077-42c6-b28d-846fcb17d8f0)
![image](https://github.com/bchiek/SimpleFileSort/assets/99049187/9482658c-374f-4d38-a90d-754f23d372ce)


## Note

The script does not move directories, only files. It also does not handle hidden files or files that it does not have permission to move.
