import requests
import json
import urllib3

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


if  __name__ == "__main__":
    
    name = input('What is the username for the user;s VPN account: ')
    p =Update_Password(name, 0)
    print(p.check_username())




