import requests 
from requests import Response
from io import StringIO 
from csv import DictReader 

url = 'https://data.ntpc.gov.tw/api/datasets/75abd5e2-5454-4c59-973f-ba587ef94ccd/csv?page=0&size=1000'

r:Response = requests.request('GET',url)
if r.status_code == 200:
    print("下載成功")
    file = StringIO(r.text)
    reader = DictReader(file)
    list_reader:list[dict] = list(reader)
    print(list_reader)

else:
    print("下載有問題")