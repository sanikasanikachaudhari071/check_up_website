# Website Check Monitor

A simple Python script that monitors website availability and sends email notifications with the results.

## Features

- Checks multiple websites for availability
- Sends email notifications with check results
- Handles connection errors and timeouts gracefully
- Can be run directly via VBS script on Windows

## Prerequisites

- Python 3.x
- Gmail account with App Password enabled
- Required Python packages (see Installation)

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd check_up_website
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project directory with your email credentials:
```
  email = your@email.com
  password = app-password from your gmail
```
## Note 
Edit your 'websites_to_check' list to add your own websites

## how to use 

### method 1:
    ```bash
    python check.py
    '''

### method 2:
  add the direct_run.vbs file in the startup folder 
  for windows:
    win+r and type shell:startup
    then add this .vbs file in this folder
## How it works :
 - It scipt check for each website if it is up or down
 - it checks if down then what is the reason
 - then complies everything and sends the mail

## output:
 --
 website check results https://www.google.com is up
https://www.youtube.com is up
https://thissitedoesnotexist.com is down (connection error)
https://www.github.com is up

this will be the expected output in the mail 

