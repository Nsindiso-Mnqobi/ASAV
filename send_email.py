# import the smtplib module. It should be included in Python by default
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='192.168.101.60', port=25)
s.starttls()
s.login("nsindiso.matshanga@econet.co.zw", "Bulawayo.6053")


sender_email = "nsindiso.matshanaga@econet.co.zw"  # Enter your address
receiver_email = "nsindiso.matshanga@yahoo.com"  # Enter receiver address
message = """\
Subject: Hi there

This message is sent from Python."""

s.sendmail(sender_email, receiver_email, message)


