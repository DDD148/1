import requests

def get_weather(city="南京"):
    url = f"https://wttr.in/{city}?format=3"
    headers = {"User-Agent":"curl"}
    res = requests.get(url, headers=headers, timeout=10)
    if res.status_code == 200:
        print(res.text)
    else:
        print("获取失败")

if __name__ == "__main__":
    get_weather("南京")
