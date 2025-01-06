

from app.schemas.user import UserCreate
from app.services.user_service import create_user


def test_create_user(client):
    
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    
    response = client.post("/api/v1/users/create", json=user_data)
    
    assert response.status_code == 200
        
    response_data = response.json()
    
    assert "id" in response_data
    assert response_data["username"] == user_data["username"]
    assert response_data["email"] == user_data["email"]
    assert response_data["is_active"] == True


async def test_get_user(client, db_session):
    user_data = UserCreate(
        username="createuser",
        email="createuser@example.com",
        password="testpassword"
    )

    # Create user (await the async function)
    await create_user(user_data, db_session)

    # Fetch the user via API
    response = client.get(f"/api/v1/users/user?username={user_data.username}")
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    response_data = response.json()

    # Validate the response
    assert "id" in response_data
    assert response_data["username"] == user_data.username
    assert response_data["email"] == user_data.email
    assert response_data["is_active"] is True

