import os

import requests
from PIL import Image
from IPython.display import IFrame

url = 'https://www.ibm.com/'

response = requests.get(url)

print(response.status_code)

header = response.headers
print(header['date'])
print(header['content-type'])