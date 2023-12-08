import requests
import os
import hashlib
from zipfile import ZipFile

url_iris = 'https://archive.ics.uci.edu/static/public/53/iris.zip'

iris_hash = 'd11fe30213d36434a0879aab7cb00ce3c812eb7ba2495874438abff7b7b762e9'

try:
    response_iris = requests.get(url_iris)
    response_iris.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error")
    print(errh.args[0])
print(response_iris)

with open('data/iris.zip', mode = 'wb') as f:
    f.write(response_iris.content)

filename_iris = 'data/iris.zip'

with open(filename_iris, 'rb') as f:
    data_iris = f.read()
    hash = hashlib.sha256(data_iris).hexdigest()
    if (hash == iris_hash):
        print('Hash matches on the Iris Dataset')
    else:
        print('Hash does not match on Iris Dataset')

print('Extracting Iris data fromm zip')

with ZipFile(filename_iris, 'r') as zObject:
    zObject.extractall(path='data/iris')


#if os.path.exists('../data/iris.zip'):
#    os.remove('../data/iris.zip')
#else:
#    print('file not found')

print('Done!')

