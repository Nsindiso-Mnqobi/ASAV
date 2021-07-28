import requests
import json
import urllib3
import win32com.client
from password_generator import PasswordGenerator

class  Update_Password:
    name = ""
    password = ""

    def __init__(self,name,password):
        self.name = name
        self.password =password

    def check_username(self):
       base_url = "https://192.168.42.50/api/objects"
       end_url = "/localusers/" + self.name

       headers =  {
        'Authorization': 'Basic YWRtaW46YnVsYXdheW8=',
         'Content-Type' : 'application/json',
         'User-Agent': 'REST API Agent',
         'Accept': 'application/json'
        }

       urllib3.disable_warnings()
       check= requests.get(url=base_url+end_url, headers=headers, verify=False).json()


       if self.name == check['name']:
             return True
       else:
            return False

    def genrate_password(self):

        pwo = PasswordGenerator()
        pwo.minlen = 8 # (Optional)
        pwo.maxlen = 10 # (Optional)
        pwo.minuchars = 1 # (Optional)
        pwo.minlchars = 4 # (Optional)
        pwo.minnumbers = 2 # (Optional)
        pwo.maxchars = 2 # (Optional)

        power =pwo.generate()
        print(power)
        return power

    def update_password(self):

        base_url = "https://192.168.42.50/api/objects"
        end_url = "/localusers/" + self.name

        headers =  {
         'Authorization': 'Basic YWRtaW46YnVsYXdheW8=',
         'Content-Type' : 'application/json',
         'User-Agent': 'REST API Agent',
         'Accept': 'application/json'
         }

        with open('update_password.json', 'r') as json_data:
            json_data = json.load(json_data)
            json_data['name'] = self.name
            json_data['password'] = self.password
            json_data['objectId'] = self.name

        with open('update_password.json', 'w') as f:
            json.dump(json_data,f, indent=4)

        with open('update_password.json', 'r') as p:
            data = p.read()
            urllib3.disable_warnings()
            check= requests.put(url=base_url+end_url ,headers=headers, data=data, verify=False)
            return check

    def send_email(self, email):
        email = ""
        outlook = win32com.client.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = email
        mail.Subject = 'VPN Credentials'
        mail.HTMLBody = '<h3>This is HTML Body</h3>'
        mail.Body = "Good Day \n \n" +"Your new vpn password is \n" +"Password: " + self.password + "\n \n Regards," + " \n Nsindiso M Matshanga"
        mail.CC = 'nsindiso.matshanga@yahoo.com'
        mail.Send()
        print("Credentials have been sent to the user")


    def save_password(self):
            base_url = "https://192.168.42.50/api/"
            end_url = "commands/writemem"

            headers =  {
                'Authorization': 'Basic YWRtaW46YnVsYXdheW8=',
                'Content-Type' : 'application/json',
                'User-Agent': 'REST API Agent',
                'Accept': 'application/json'
                }

            urllib3.disable_warnings()
            save = requests.post(url=base_url+end_url, headers=headers, verify=False).json()

            print("Configuration has been saved")

if  __name__ == "__main__":

    name = input('What is the username for the user;s VPN account: ')
    check =Update_Password(name, 0)
    check.check_username()

    if check.check_username() == True:
        password = check.genrate_password()
        email_address = input("Please type clients email address: ")
        update = Update_Password(name, password)
        update.update_password()
        update.send_email(email_address)
        update.save_password()