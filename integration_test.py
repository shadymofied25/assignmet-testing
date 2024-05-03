from app import create_app, User
def test_user_registration():
  app = create_app('testing') 
  with app.app_context():
 
    user = User(username="test_user", email="test@example.com", password="password")
    db.session.add(user)
    db.session.commit()


    registered_user = User.query.filter_by(username="test_user").first()
    assert registered_user is not None

def teardown_module():

  pass
