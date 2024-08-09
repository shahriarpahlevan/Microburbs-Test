import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Configuration
news_api_key = 'YOUR_NEWS_API_KEY'  # Replace with your NewsAPI key
recipient_email = 'daniel@thefullwiki.org'
sender_email = 'shahpahlevan@gmail.com'
sender_password = 'abc123'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Fetch today's news headlines from Australia
url = f"https://newsapi.org/v2/top-headlines?country=au&apiKey={news_api_key}"
response = requests.get(url)
news_data = response.json()

# Extracting the headlines
headlines = []
if news_data['status'] == 'ok':
    articles = news_data['articles']
    headlines = [article['title'] for article in articles]

# Create the email content
email_subject = f"Today's News Headlines - {datetime.now().strftime('%Y-%m-%d')}"
email_body = "Here are today's top news headlines from Australia:\n\n"
email_body += "\n".join(headlines)

# Send the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = email_subject

msg.attach(MIMEText(email_body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()
    print(f"Email sent successfully to {recipient_email}")
except Exception as e:
    print(f"Failed to send email. Error: {str(e)}")