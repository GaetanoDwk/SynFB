# v. 1.0.0
from datetime import datetime
import string
import smtplib
import datetime

class Mail:

# SMTP OPERATIONS
    # Send e-mail via SMTP
    def send_mail(self, smtp, port, user, pasw, to, msg):
        try:
            # This line it's for SMTP over standard port 25.
            m = smtplib.SMTP(smtp, port)
            # This line it's for SMTP over SSL. If you enable it you've to disable prev line (over port 25).
            # m = smtplib.SMTP_SSL(smtp, port)
            m.ehlo()
            m.login(user, pasw)
            m.sendmail(user, to, msg)
            m.quit()
            return 1
        except Exception as e:
            return e

# OTHER
    # Generate mail content
    def crea_messaggio_mail(self, header, to, subject, messaggio):
        try:
            msg = string.join((
                "Date: %s" % header,
                "From: SynFB",
                "To: %s" % to,
                "Subject: %s" % subject,
                "",
                messaggio,
            ), "\r\n")
            return msg
        except Exception as e:
            print e
            msg = self.create_exception_mail(self.USER, 'EXCEPTION SynFB', 'SynFB.py', e)
            self.send_mail(self.SMTP, self.PORT, self.USER, self.PWD, self.USER, msg)
            return e

    def create_exception_mail(self, to, subject, func, e):
        try:
            header = datetime.datetime.now()
            messaggio = '%s\nEXCEPTION %s: %s' % (header, func, e)
            msg = string.join((
                "Date: %s" % header,
                "From: Mail Monitor",
                "To: %s" % to,
                "Subject: %s" % subject,
                "",
                messaggio,
            ), "\r\n")
            return msg
        except Exception as e:
            msg = self.create_exception_mail(self.USER, 'EXCEPTION MailMonitor', 'create_exception_mail', e)
            self.send_mail(self.SMTP, self.PORT, self.USER, self.PWD, self.USER, msg)
            print e