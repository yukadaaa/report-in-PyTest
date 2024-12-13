from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {}

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

@app.post("/user")
def create_user(user_id: int, name: str, role: str):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User ID already exists")
    users[user_id] = {"name": name, "role": role}
    return {"message": "User created"}

@app.get("/user")
def get_users():
    return users

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted"}
