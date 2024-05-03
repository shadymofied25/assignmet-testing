# # Imports
# import pytest
# from app import create_app
# from app.models import User  # Assuming models are imported

# # Fixture to create a test app
# @pytest.fixture
# def test_app():
#   app = create_app('testing')
#   with app.app_context():
#     yield app  # Execute tests with the app context
#   # Clean up after tests (e.g., drop database tables)

# # Test user registration API endpoint
# def test_register_api(test_app):
#   client = test_app.test_client()
#   data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'password'}
#   response = client.post('/api/register', json=data)
#   assert response.status_code == 201  # Created

#   # Check if user is registered in the database
#   user = User.query.filter_by(username='test_user').first()
#   assert user is not None
