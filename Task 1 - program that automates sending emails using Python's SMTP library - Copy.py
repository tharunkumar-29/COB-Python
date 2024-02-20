import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("Email sent successfully")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed.")
    except smtplib.SMTPException as e:
        print("Error:", e)

def get_user_input():
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    receiver_email = input("Enter recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")

    print("\nSelect SMTP server:")
    print("1. Gmail")
    print("2. Outlook")
    smtp_choice = input("Enter your choice (1 or 2): ")
    smtp_server, smtp_port = '', 0
    if smtp_choice == '1':
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
    elif smtp_choice == '2':
        smtp_server = 'smtp.office365.com'
        smtp_port = 587
    else:
        print("Invalid choice. Using default SMTP server (Gmail).")
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

    return sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port

def main():
    sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port = get_user_input()
    send_email(sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port)

if __name__ == "__main__":
    main()
