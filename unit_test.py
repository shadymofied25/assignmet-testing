
from app import User, LoginForm, RegisterForm


def test_user_init(app):
  with app.app_context():
    user = User(username="test_user", email="test@example.com", password="password")
    assert user.username == "test_user"
    assert user.email == "test@example.com"
    assert user.password_hash is not None 


def test_login_form_validation():
  form = LoginForm()
  assert not form.validate_on_submit()  

  form.username.data = "test_user"
  assert not form.validate_on_submit()  
  form.password.data = "password"
  assert form.validate_on_submit() 

def test_register_form_validation():
  form = RegisterForm()
  assert not form.validate_on_submit()  
 
