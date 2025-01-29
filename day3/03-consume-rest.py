# consume rest APIs 
# pip install requests 

# import requests
# api_url = 'https://jsonplaceholder.typicode.com/users/1'
# response =  requests.get(api_url)
# data = response.json()
# print(data['name'], data['email'])

import requests

api_url = 'https://jsonplaceholder.typicode.com/users/1'

try: 
    response =  requests.get(api_url)

except requests.exceptions.ConnectionError as e:
    print('exception occured and handled')
    
else:    
    data = response.json()
    print(data['name'], data['email'])
    
finally:
    response.close()
    
    print('done')

