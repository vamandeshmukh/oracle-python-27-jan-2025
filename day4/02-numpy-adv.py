# numpy array of strings 

import requests as rq
import numpy as np

api_url = 'https://jsonplaceholder.typicode.com/posts'
response = rq.get(api_url)
data = response.json()
# print(data)

arr = np.array([d['title'] for d in data])

raw_list = arr.tolist()
for r in raw_list:
    print(r)

# print(arr.size)
# print(arr.shape)
# print(arr.dtype)
# print(np.char.upper(arr))
# print(np.char.find(arr, 'e'))
# print(np.char.split(arr, ' '))
#  "title": "at nam consequatur ea labore ea harum",
# list(['at', 'nam', 'consequatur', 'ea', 'labore', 'ea', 'harum'])]
# print(np.sort(arr))