from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
  wait_time = between(1, 2) 

  @task
  def index(self):
    self.client.get("/") 

  @task(weight=2)  
   

  def on_start(self):
    
    pass
