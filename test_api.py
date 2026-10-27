import api_client

def test_create_post():
    payload = {
        "title": "Тестовый заголовок",
        "body": "Тестовый текст поста",
        "userId": 1
    }
    response = api_client.create_post(payload)
    
    assert response.status_code == 201
    
    res_data = response.json()
    assert res_data["title"] == payload["title"]
    assert res_data["body"] == payload["body"]
    assert res_data["userId"] == payload["userId"]
    assert "id" in res_data

def test_update_post():
    post_id = 1
    payload = {
        "id": post_id,
        "title": "Обновленный заголовок",
        "body": "Обновленный текст поста",
        "userId": 1
    }
    response = api_client.update_post(post_id, payload)
    
    assert response.status_code == 200
    
    res_data = response.json()
    assert res_data["title"] == payload["title"]
    assert res_data["body"] == payload["body"]
    assert res_data["id"] == post_id

def test_delete_post():
    post_id = 1
    response = api_client.delete_post(post_id)
    
    assert response.status_code == 200
    assert response.json() == {}

def test_get_comments():
    response = api_client.get_comments(1)
    
    assert response.status_code == 200
    
    res_data = response.json()
    assert isinstance(res_data, list)
    assert len(res_data) > 0
    
    first_comment = res_data
    assert "postId" in first_comment
    assert "id" in first_comment
    assert "name" in first_comment
    assert "email" in first_comment
    assert "body" in first_comment

def test_get_non_existent_post():
    response = api_client.get_post(999)
    
    assert response.status_code == 404
    assert response.json() == {}
