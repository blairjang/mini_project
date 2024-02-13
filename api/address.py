import requests

key = ""
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

# address_name : 주소
# category_name : 분류("가정,생활 > 결혼 > 예식장")
# id : 아이디
# phone : 전화번호
# place_name : 상호 명
# place_url : url 주소
# road_address_name': 도로명 주소
# x : 경도
# y : 위도