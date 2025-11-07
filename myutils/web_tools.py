import requests

def get_ip_info(ip_address: str) -> dict:
    url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,regionName,city,isp,query"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"status": "fail", "message": f"请求失败: {e}"}
