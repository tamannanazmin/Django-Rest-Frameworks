import requests

'''url ="http://127.0.0.1:8000/api/users_list/"
response=requests.get(url)
print(response.text)'''

def get_token():
    #Get_auth token
    url ="http://127.0.0.1:8000/api/auth/"
    response=requests.post(url,data={'username':'tamanna',
                                 'password': '123456'})
    return response.json()
#get_token()

def get_data():
    url="http://127.0.0.1:8000/api/user_list/"
    header= {'Authorization' : f'Token{get_token()}'}
    response = requests.get(url,headers=header)
    #emp_data=response.json()
    #for e in emp_data:
     #   print(e)
    print(response.text)
get_data()