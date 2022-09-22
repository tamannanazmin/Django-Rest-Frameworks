import requests

'''url ="http://127.0.0.1:8000/api/users_list/"
response=requests.get(url)
print(response.text)'''
URL= "http://127.0.0.1:8000"
def get_token():
    #Get_auth token
    url =f"{URL}/api/auth/"
    response=requests.post(url,data={'username':'tamanna',
                                 'password': '123456'})
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        return response.json()
    #return response.json()
#get_token()

def get_data():
    url=f"{URL}/api/user_list/"
    header= {'Authorization' : f'Token{get_token()}'}
    response = requests.get(url, headers=header)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        emp_data = response.json()
        for e in emp_data:
            print(e)
    #print(response.json())
get_data()

def create_new(count):
    url=f"{URL}/api/user_list/"
    header= {'Authorization': f'Token{get_token()}'}
    data={
        "employee_id": f"HQ00{count}",
        "name": "Raziv",
        "age": 28,
        "ranking": 2.4
    }
    response=requests.post(url, data=data, headers=header)
    print(response.text)
for e in range(20):
    create_new(e)