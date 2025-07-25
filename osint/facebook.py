import requests

ACCESS_TOKEN = "YOUR_FACEBOOK_ACCESS_TOKEN"

def search_user(name):
    url = "https://graph.facebook.com/v18.0/search"
    params = {
        "q": name,
        "type": "user",
        "access_token": ACCESS_TOKEN
    }
    res = requests.get(url, params=params)
    return res.json().get("data", [])

def get_user_profile(user_id):
    url = f"https://graph.facebook.com/v18.0/{user_id}"
    params = {
        "fields": "id,name,link,location,picture.type(large)",
        "access_token": ACCESS_TOKEN
    }
    res = requests.get(url, params=params)
    return res.json()

def get_user_timeline(user_id):
    url = f"https://graph.facebook.com/v18.0/{user_id}/posts"
    params = {
        "fields": "message,created_time",
        "access_token": ACCESS_TOKEN
    }
    res = requests.get(url, params=params)
    return res.json().get("data", []) if res.status_code == 200 else []

