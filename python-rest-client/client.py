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
get_data()
def create_new(count):
    # using this you can entry data as much as you want at the same time other than one by one
    url = f"{URL}/api/users_list/"
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "employee_id": f"HQ00{count}",
        "name": "Tamanna Nazmin",
        "age": 30,
        "ranking": 0.5,
        #"photo": "/hrm/photo/download.jfif",
        #"resume": "/hrm/file/download.jfif"
    }
    response = requests.post(url, data=data, headers=header)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        print(response.text)
#for e in range(30):
    create_new(30)

def edit_data(employee_id):
    # this can be used to update data
    url = f"{URL}/api/users_list/{employee_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        "name": "Editing data",
        "age": 30,
        "ranking": 0.5,
        #"photo": "/hrm/photo/download.jfif",
        #"resume": "/hrm/file/download.jfif"
    }
    response = requests.put(url, data=data, headers=header)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        print(response.text, response.status_code)
#edit_data(2)

def delete_data(employee_id):
    # this can be used to delete data
    url = f"{URL}/api/users_list/{employee_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.delete(url, headers=header)
    #response.raise_for_status()  # raises exception when not a 2xx response
    #if response.status_code != 204:
    print(response.status_code)

'''for e in range(5,20):
    delete_data(e)'''