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
        return (response.json())
    #return response.json()
#get_token()

def get_data():
    url = f"{URL}/api/users_list/"
    header = {'Authorization': f'Token {get_token()}'}
    response= requests.get(url, headers=header)
    emp_data = response.json()
    for e in emp_data:
        print(e)
    #print(response.json())
#get_data()
def create_new():
    # using this you can entry data as much as you want at the same time other than one by one
    url = "http://127.0.0.1:8000/api/users_list/"
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "employee_id": "HQ005",
        "name": "Prashun Roy",
        "age": 30,
        "ranking": 0.5
        #"photo": "/hrm/photo/download.jfif",
        #"resume": "/hrm/file/download.jfif"
    }
    response = requests.post(url, data=data, headers=header)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        print(response.text)
create_new()