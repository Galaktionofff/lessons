from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
users = []


# uvicorn module_16_3:app --reload
class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
def get_users() -> list[User]:
    return users


@app.post('/users/{username}/{age}')
def append_user(username: str, age: int, user: User) -> User:
    user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/users/{user_id}/{username}/{age}')
def put_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.username, edit_user.age = username, age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail=("User was not found"))


@app.delete('/user/{user_id}')
def delete(user_id: int) -> User:
    try:
        del_u = users.pop(user_id - 1)
        return del_u
    except IndexError:
        raise HTTPException(status_code=404, detail=("User was not found"))
