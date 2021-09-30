import os
import smtplib
from email.message import EmailMessage

def sending_df():
    """Sending specific dataframe to Email"""
    EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

    msg = EmailMessage()
    msg['Subject'] = "WDR2-Playlist-Check"
    msg['From'] = EMAIL_ADDRESS
    msg["To"] = "kwieeee@gmail.com"
    msg.set_content("Image attached")

    files = ["test_wdr2.csv"]

    for file in files:
        with open(file, "rb") as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

