directory = os.getcwd()
for i in os.walk('.'):
    print(i)
print(os.path.join('/Users/nikitagalaktionov/PycharmProjects/Urban/NameSpace/module_7/module_7_2.py'))
print(time.ctime(os.path.getmtime('module_7_1.py')))
print(os.path.getsize('module_7_1.py'))
print(os.path.dirname('/Users/nikitagalaktionov/PycharmProjects/Urban/NameSpace/module_7/module_7_1.py'))

