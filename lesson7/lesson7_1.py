import requests 
from requests import Response
from requests import RequestException, HTTPError 
from io import StringIO 
from csv import DictReader 

url = 'https://data.ntpc.gov.tw/api/datasets/75abd5e2-5454-4c59-973f-ba587ef94ccd/csv?page=0&size=1000'

try:
    r:Response = requests.request('GET',url)
    r.raise_for_status()
except HTTPError as e:
    print(e)
except RequestException as e:
    print(e)
else:
    print("下載成功")
    file = StringIO(r.text)
    reader = DictReader(file)
    list_reader:list[dict] = list(reader)
    print(list_reader)

