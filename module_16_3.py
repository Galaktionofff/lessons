from fastapi import FastAPI, Path
from typing import Annotated

# uvicorn module_16_2:app --reload

users = {'1': 'Имя: Example, возраст: 18'}
app = FastAPI()


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.put('/user/{user_id}/{username}/{age}')
async def get_message(username: str, age: int, user_id: int) -> str:
    
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.post('/user/{username}/{age}')
async def create_message(username: str, age: int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.delete('/user/{user_id}')
async def delete(user_id: Annotated[str, Path(min_length=0, max_length=20)]):
    users.pop(user_id)
