from os import read
import requests
import json
import urllib3

url = "https://graph.microsoft.com/v1.0/me/sendMail"

headers = {
         'Accept': 'application/json',
         'Content-type': 'application/json',
         'Authorization': 'eyJ0eXAiOiJKV1QiLCJub25jZSI6ImowZkdUSTBCaFdPRHdka2l1RlM3c0txd2dHaUYxaU1KbjFlSlVLZWU0NkUiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zZDMxZGY0MC03YzE1LTQzZjUtOGNjOC1lM2RkZTVhMjdlMTUvIiwiaWF0IjoxNjI5NTA4NjMxLCJuYmYiOjE2Mjk1MDg2MzEsImV4cCI6MTYyOTUxMjUzMSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkUyWmdZSGdybHRmNzQ2bDBLK2ZyWGo1dWR3K2hqdStGc2J3VngrdU9MZUgydUtpeld4Z0EiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6Ik1hdHNoYW5nYSIsImdpdmVuX25hbWUiOiJOc2luZGlzbyIsImlkdHlwIjoidXNlciIsImlwYWRkciI6Ijc3LjI0Ni41Mi4xMjkiLCJuYW1lIjoiTnNpbmRpc28gTWF0c2hhbmdhIiwib2lkIjoiODk1OGY5ZTEtMWRkOS00NjIxLWJiM2UtN2IwMjg5ZDkxMzYyIiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTQwODY0MjY4MzktMjE5NDMyODkwMi05Mzk4NjgxMzAtMTQ3MDA0IiwicGxhdGYiOiIzIiwicHVpZCI6IjEwMDMyMDAwOUFGQkU5RUEiLCJyaCI6IjAuQVNFQVFOOHhQUlY4OVVPTXlPUGQ1YUotRmJYSWk5NzUyYkZJcUsyM1NOcHlVR1FoQUJjLiIsInNjcCI6Ik1haWwuUmVhZCBNYWlsLlNlbmQgTWFpbC5TZW5kLlNoYXJlZCBvcGVuaWQgcHJvZmlsZSBVc2VyLlJlYWQgZW1haWwiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJhOXFKRFdZT1BTZjhOSjA0TDRiU1VOMzY4d0xsRVV4SzY3dFZQdmwwaXdrIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkFGIiwidGlkIjoiM2QzMWRmNDAtN2MxNS00M2Y1LThjYzgtZTNkZGU1YTI3ZTE1IiwidW5pcXVlX25hbWUiOiJOc2luZGlzby5NYXRzaGFuZ2FAZWNvbmV0LmNvLnp3IiwidXBuIjoiTnNpbmRpc28uTWF0c2hhbmdhQGVjb25ldC5jby56dyIsInV0aSI6IjhRM2xfVC1jaFVXa1JHbDdqX05VQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiUll2MG91VFdDdC1lM0piOTlhQ2NfVWtBUFh6Nk1PNlBUcXo0T1h3VFNQOCJ9LCJ4bXNfdGNkdCI6MTUxMDIyNDIzMn0.QDkmdM_UcE4bdu_5gTM6ZZMBc6xGfySfHckaSOYGl5ORDibEVHnHVVSEqL9-SbPJcvRPWKa4HJ94L4mwfuWrQLqmv7CzDrrnVAgtzCRwLowurO0O1SlPLAHx1CGJbHqn4RR0YCn6OER2s5ryxIuQk5ptI79ILJzly14QEBsbONNnAFamBuHSvi116wxN9Zgt5vPGQSoVdkY0hYfdZai16hwc-lexTK2gFLdTHdo99QoYk7TnDbIsf1EbFkC2oHesNY5ePJNmlZrc0eW_MCJ1E0nHo_7TSDBP8pNj-aCrKrMGIGSBMixNUMYgK4B-3iTrsI2gWeuVg4XnJ-NrAI5Liw'
    }

with open('send_mail.json', 'r') as json_data:
    json_data = json.load(json_data)
    print(json_data)
    json_data["message"]["toRecipients"][0]["emailAddress"]["address"] = "nsinmatsh@gmail.com"
    json_data["message"]["body"]["content"] = "Good Day "+ "kli" + "\n\nYour vpn credentials are \n"+"Username: "+ "joy" +"\nPassword: " + "player" + "\n\nRegards," + "\nNsindiso M Matshanga"

with open('send_mail.json', 'w') as f:
    json.dump(json_data,f,indent=2)

with open('send_mail.json', 'r') as p:
    data=p.read()
    response = requests.post( url, headers=headers, data=data)
    Final = response.status_code

    if Final == "202":
        print("Email has been sent to user")
    else:
        print(Final)
        print("The email has not been sent.")