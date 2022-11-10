import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from com.dino.stocktracker.config import *

# Setup port number and server name

smtp_port = 587
smtp_server = "smtp.gmail.com"

# Set up the email lists
email_from = mymail
email_list = mail_list

pwd = my_pwd

# dateTimeObj = datetime.now()
# timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M)")
# print('Current Timestamp : ', timestampStr)

# subject of email
subject = 'Narrow CPR Stock Alert: '


# Define the email function (dont call it email!)
def send_emails(email_list):
    for person in email_list:
        # Make the body of the email
        body = f"""
        
        Hello!
        
        Greetings for the day!
                
        Narrow CPR data has been generated for the stocks and attached here!
        
        Thanks,
        MyPy Bot
        """

        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        filename = "nrcpr.csv"
        print(filename)

        # Open the file in python as a binary
        attachment = open(dataset_path + filename, 'rb')

        # Encode as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload(attachment.read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pwd)
        print("Successfully connected to server")
        print()

        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    TIE_server.quit()


# Run the function
send_emails(email_list)
