import requests
import socket
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

email = os.getenv("email")
password = os.getenv("password")

webites_to_check = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://thissitedoesnotexist.com",
    "https://www.github.com"
]

def send_mail(message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = "Website Check Results"
        msg['From'] = email
        msg['To'] = email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error sending mail: {e}")

def check_website():
    results = []
    for url in webites_to_check:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{url} is up")
                results.append(f"{url} is up")
            else:
                print(f"{url} is down (status code: {response.status_code})")
                results.append(f"{url} is down (status code: {response.status_code})")
        except (requests.ConnectionError, requests.Timeout):
            print(f"{url} is down (connection error)")
            results.append(f"{url} is down (connection error)")
    print("All websites checked")
    return results

if __name__ == "__main__":


    
    websites_results = check_website()
    email_message = "website check results"
    for result in websites_results:
        email_message += f"{result}\n"
    send_mail(email_message)