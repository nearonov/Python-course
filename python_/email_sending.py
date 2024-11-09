from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

html_templates = Template(Path("templates/index.html").read_text())
html_content = html_templates.substitute({'name': 'Eugene'})  # 'name'-змінна для index.html $name
my_email = EmailMessage()

my_email['from'] = 'Eugene'
my_email['to'] = 'ayvengo85@gmail.com'
my_email['subject'] = "Hello from  Python"
my_email.set_content(html_content, "html")

with open("images/545.jpg", 'rb') as img:#відправка фото
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image', subtype='jpg', filename='545.jpg')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp_server:
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login('storeserver17@gmail.com', 'dsjy muck oquu gjdl')
    smtp_server.send_message(my_email)
    print("Жека привіт!")


# with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
#     smtp_server.ehlo()
#     smtp_server.send_message(my_email)
#     print("Жека привіт!")
