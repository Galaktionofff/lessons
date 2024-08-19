def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()
inner_function()
# inner_function() не работает, ведь находится в локальном пространстве имен test_function()