import requests

resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    print(data_model)  # 打印返回的 JSON 数据
else:
    print(f"Failed to retrieve data. Status code: {resp.status_code}")