import requests


url = "https://dapi.kakao.com/v2/local/search/keyword.json"
headers = {
    "Authorization": "KakaoAK "+key,
    "content-type": "application/json;charset=UTF-8"
}
params = {
    "query" : "예식",    
    
}
data = requests.get(url, params=params, headers=headers).json()["documents"]
print(data)
