import requests

BASE_URL = "https://typicode.com"

def create_post(payload):
    return requests.post(f"{BASE_URL}/posts", json=payload)

def update_post(post_id, payload):
    return requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)

def delete_post(post_id):
    return requests.delete(f"{BASE_URL}/posts/{post_id}")

def get_comments(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}/comments")

def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")
