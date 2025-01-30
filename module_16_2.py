from fastapi import FastAPI, Path
from typing import Annotated

# uvicorn module16:app --reload
# uvicorn module16:app --reload --port 8080
app = FastAPI()


@app.get('/')
async def main():
    text = "Главная страница"
    return text


@app.get('/user/admin')
async def admin():
    text = 'Вы вошли как администратор'
    return text


@app.get('/user/{username}/{age}')
async def users_id(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')]
                   , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]):
    text = f'Информация о пользователе. Имя: {username}, Возраст: {age}'
    return text


@app.get('/userid/{id}')
async def user(id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=3)]):
    text = f'Вы вошли как пользователь №{id}'
    return text
