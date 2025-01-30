# numpy array of strings 

import requests as rq
import numpy as np

api_url = 'https://jsonplaceholder.typicode.com/posts'
response = rq.get(api_url)
arr = np.array([d['title'] for d in response.json()])
print(arr)