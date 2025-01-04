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
print(response.encoding)
# print(response.text[0:100])
# Image
url2 = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN'
        '-SkillsNetwork/IDSNlogo.png')

res = requests.get(url2)

path = os.path.join(os.getcwd(), 'image.png')

with open(path, 'wb') as f:
    f.write(res.content)

print(Image.open(path))