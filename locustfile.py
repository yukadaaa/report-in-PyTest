from locust import HttpUser, task

class FastAPILoadTest(HttpUser):

    @task
    def root_endpoint(self):
        self.client.get("/")

    @task
    def create_user(self):
        self.client.post("/user", json={"user_id": 1, "name": "Alice", "role": "admin"})

    @task
    def get_users(self):
        self.client.get("/user")

    @task
    def get_user(self):
        self.client.get("/user/1")

    @task
    def delete_user(self):
        self.client.delete("/user/1")
