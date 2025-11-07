import requests

def get_ip_info(ip_address: str) -> dict:
    """使用免费API查询IP地理信息"""
    url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,regionName,city,isp,query"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"status": "fail", "message": f"请求失败: {e}"}

# 天气API (例如 OpenWeatherMap) 大多需要 API Key
# 你可以自己注册一个免费key，然后在这里实现它
def get_weather(city: str, api_key: str) -> dict:
    """(示例) 查询天气，需要API Key"""
    if not api_key:
        return {"status": "fail", "message": "未提供 API Key"}
    # ... (此处省略调用天气API的逻辑) ...
    return {"status": "success", "city": city, "weather": "晴"}