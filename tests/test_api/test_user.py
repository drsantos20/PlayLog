

from fastapi.testclient import TestClient
from app.db.models.user import User
from app.main import app

client = TestClient(app)

def test_create_user(db_session):
    
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    
    new_user = User(
        username=user_data["username"],
        email=user_data["email"],
        hashed_password=user_data["password"]  # In real use, hash the password
    )
    db_session.add(new_user)
    db_session.commit()
    
    response = client.post("/api/v1/users/create", json=user_data)
    
    assert response.status_code == 200
        
    response_data = response.json()
    
    assert "id" in response_data
    assert response_data["username"] == user_data["username"]
    assert response_data["email"] == user_data["email"]
    assert response_data["is_active"] == True
