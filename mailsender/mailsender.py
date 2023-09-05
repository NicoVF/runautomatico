import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailSender:
    def __init__(self, username, password, server='smtp.gmail.com', port=587, use_tls=True):
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.use_tls = use_tls

    def send(self, sender, receivers, subject, message='', images=None):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(receivers)
        self._get_msg_text(message, msg)
        if images:
            self._get_msg_images(images, msg)
        self._send_msg(msg, receivers, sender)

    def _send_msg(self, msg, recipients, sender):
        server = smtplib.SMTP('{0}:{1}'.format(self.server, self.port))
        try:
            if self.use_tls:
                server.starttls()
            server.login(self.username, self.password)
            server.sendmail(sender, recipients, msg.as_string())
        finally:
            server.quit()

    def _get_msg_images(self, images, msg):
        for image in images:
            with open(image, 'rb') as f:
                msg_image = MIMEImage(f.read())
                msg_image.add_header('Content-Disposition', 'attachment',
                                     filename=image.split('/', 2)[1].replace('.', ':'))
                msg.attach(msg_image)

    def _get_msg_text(self, message, msg):
        msg_text = MIMEMultipart()
        text = MIMEText(message)
        msg_text.attach(text)
        msg.attach(msg_text)


