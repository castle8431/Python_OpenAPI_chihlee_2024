import requests 
from requests import Response
from requests import RequestException, HTTPError
from io import StringIO 
from csv import DictReader 
import streamlit as st

@st.cache_data #暫存資料 沒有改變的資料不用重複rerun 增加效能
def get_youbikes()->list[dict]:

    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'

    try:
        r:Response = requests.request('GET',url)
        r.raise_for_status()
    except HTTPError as e:
        raise Exception("伺服器有問題")
    except RequestException as e:
        raise Exception("連線有問題")
    else:
        print("下載成功")
        file = StringIO(r.text)
        reader = DictReader(file)
        list_reader:list[dict] = list(reader)
        return list_reader