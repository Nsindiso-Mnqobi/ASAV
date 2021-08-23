from os import close
from password_generator import PasswordGenerator
from netmiko import ConnectHandler
import requests
import json
import urllib3

class  Update_Password:
    name = ""
    username = ""
    password = ""
    email = ""

    def __init__(self, name, password, email,username):
        self.name = name
        self.password =password
        self.email = email
        self.username= username
        
    def generate_password(self):
        
        pwo = PasswordGenerator()
        pwo.minlen = 8 # (Optional)
        pwo.maxlen = 10 # (Optional)
        pwo.minuchars = 1 # (Optional)
        pwo.minlchars = 4 # (Optional)
        pwo.minnumbers = 2 # (Optional)
        pwo.maxchars = 2 # (Optional)

        power =pwo.generate()
        print(self.name + " new password will be " +power)
        return power

    def check_username(self):

        Device = {
            'device_type': "cisco_asa",
            'host':   "192.168.42.50",
            'username': "admin",
            'password': "bulawayo",
            'secret': "bulawayo"
        }

        net_connect = ConnectHandler(**Device)
        net_connect.enable()
        output = net_connect.send_command('show running-config username ' + self.username)
        print(output)

    def update_password(self):

        Device = {
            'device_type': "cisco_asa",
            'host':   "192.168.42.50",
            'username': "admin",
            'password': "bulawayo",
            'secret': "bulawayo"
        }

        net_connect = ConnectHandler(**Device)
        net_connect.enable()
        net_connect.config_mode()
        output = net_connect.send_command('username ' + self.username + " password " + self.password  + " privilege 0" )
        print("Password for "+self.name + " has been changed")                                       
        print("*"*80)
        print("")

    def save_password(self):
       
        Device = {
            'device_type': "cisco_asa",
            'host':   "192.168.42.50",
            'username': "admin",
            'password': "bulawayo",
            'secret': "bulawayo"
        }

        net_connect = ConnectHandler(**Device)
        net_connect.enable()
        output = net_connect.save_config()
        print("")
        print("Configuration has been saved")
        print("#"*80)

    def send_email(self):

        url = "https://graph.microsoft.com/v1.0/me/sendMail"

        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IkwxTWhYaDZfMHNCZExiX193bVI1Y09hRy1oS2JOUDY3S1FNNXFzd0I1X0kiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zZDMxZGY0MC03YzE1LTQzZjUtOGNjOC1lM2RkZTVhMjdlMTUvIiwiaWF0IjoxNjI5NzA2MDc2LCJuYmYiOjE2Mjk3MDYwNzYsImV4cCI6MTYyOTcwOTk3NiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFTUUEyLzhUQUFBQUYvakYzSWFsY0JlZmhmUWJ5RlllMjVNNHlmL29ZM3ZlZmVMdkc3TlZLRXc9IiwiYW1yIjpbInB3ZCJdLCJhcHBfZGlzcGxheW5hbWUiOiJHcmFwaCBFeHBsb3JlciIsImFwcGlkIjoiZGU4YmM4YjUtZDlmOS00OGIxLWE4YWQtYjc0OGRhNzI1MDY0IiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiJNYXRzaGFuZ2EiLCJnaXZlbl9uYW1lIjoiTnNpbmRpc28iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiI3Ny4yNDYuNDkuOCIsIm5hbWUiOiJOc2luZGlzbyBNYXRzaGFuZ2EiLCJvaWQiOiI4OTU4ZjllMS0xZGQ5LTQ2MjEtYmIzZS03YjAyODlkOTEzNjIiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNDA4NjQyNjgzOS0yMTk0MzI4OTAyLTkzOTg2ODEzMC0xNDcwMDQiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDA5QUZCRTlFQSIsInJoIjoiMC5BU0VBUU44eFBSVjg5VU9NeU9QZDVhSi1GYlhJaTk3NTJiRklxSzIzU05weVVHUWhBQmMuIiwic2NwIjoiTWFpbC5SZWFkIE1haWwuU2VuZCBNYWlsLlNlbmQuU2hhcmVkIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6ImE5cUpEV1lPUFNmOE5KMDRMNGJTVU4zNjh3TGxFVXhLNjd0VlB2bDBpd2siLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQUYiLCJ0aWQiOiIzZDMxZGY0MC03YzE1LTQzZjUtOGNjOC1lM2RkZTVhMjdlMTUiLCJ1bmlxdWVfbmFtZSI6Ik5zaW5kaXNvLk1hdHNoYW5nYUBlY29uZXQuY28uenciLCJ1cG4iOiJOc2luZGlzby5NYXRzaGFuZ2FAZWNvbmV0LmNvLnp3IiwidXRpIjoieUZWczdxM2tCVWV6M3lnN3ZfZFhBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19zdCI6eyJzdWIiOiJSWXYwb3VUV0N0LWUzSmI5OWFDY19Va0FQWHo2TU82UFRxejRPWHdUU1A4In0sInhtc190Y2R0IjoxNTEwMjI0MjMyfQ.HS9fOnm0hXL0xcmA-jqbTP_w6K4edcReWbnpPbVPnDV-kA5DT51W4914i6hG8yz9pG-JUxb1rWZrSwkBulQEEQMLM9y11Yw-qQeMn7EEY8hhf1PXl5cMPKeJ1jes8W6AJyEHRaV1Z8y_btWy5olHnw6CuyOae9QXOQ7mF2HUxF8LbeIbxl6SkHTI4vFNxtIoTVUvHpr7bOdhTHSGdg4mLNqfEPBKuEQPEyuceQIReZfeFAVZxiQETlWHCQfC3z-kfQApfdhx_LVakMai_wCm7tqRaAP7q-nCOhmJXksJ5PhlgV-NdyAzySWZYAPd9RcGK1UeO_6KaBjKTQyTFztAnw'
                }

        with open('send_mail.json', 'r') as json_data:
            json_data = json.load(json_data)
            json_data["message"]["toRecipients"][0]["emailAddress"]["address"] = self.email
            json_data["message"]["body"]["content"] = "Good Day "+ self.name + "\n\nYour vpn credentials are \n"+"Username: "+ self.username +"\nPassword: " + self.password + "\n\nRegards," + "\nNsindiso M Matshanga"

        with open('send_mail.json', 'w') as f:
                json.dump(json_data,f,indent=2)

        with open('send_mail.json', 'r') as p:
            data=p.read()
            response = requests.post( url, headers=headers, data=data)
            
            if response.status_code == "202":   
                print("Email has been sent to user")
                print("*"*80) 
            else:
                print("Email has not been sent")
                print("*"*80) 

if  __name__ == "__main__":
    
    Username = input("Please type the name of the client: ")
    name = input("What is the username for the clients VPN account: ")
    print("*"*80)
    print("")
    check =Update_Password(name, 0, "none", Username)
    check.check_username()

    print("*"*80)

    Proceed = input("Do you want to proceed with the password reset(yes/no)? ")

    print("*"*80)
    print("")

    if Proceed.lower() =="yes":
        password = check.generate_password()
        print("*"*80)
        print("")
        email_address = input("Please type the clients email address: ")
        update = Update_Password(name, password, email_address, Username)
        print("*"*80)
        print("")
        update.update_password()
        update.send_email()
        update.save_password()
    
    elif Proceed.lower()=="no":
        close() 
        
    else: 
        print("Please type yes or no")

       

