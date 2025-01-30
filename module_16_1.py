from fastapi import FastAPI

# uvicorn module16:app --reload
# uvicorn module16:app --reload --port 8080
app = FastAPI()


@app.get('/')
async def main():
    text = "Главная страница"
    entext = text.encode("utf-8")
    return entext


@app.get('/user/admin')
async def admin():
    text = 'Вы вошли как администратор'
    entext = text.encode("utf-8")
    return entext


@app.get('/user/{user_id}')
async def user(id: int):
    text = f'Вы вошли как пользователь №{id}'
    entext = text.encode("utf-8")
    return entext


@app.get('/user')
async def users_id(user: str = 'Nik', age: int = 19):
    text = f'Информация о пользователе. Имя: {user}, Возраст: {age}'
    entext = text.encode("utf-8")
    return entext
#Почему-то API не воспринимает кириллицу, я не знаю, что с этим делать
