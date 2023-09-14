quest = input('\n\tВыберите Действие \n\tрегистрация\n\tЛогин \n\t Выберите Действие : ').lower()

if quest == 'логин':
    from code_1 import login
    login()
elif quest == 'регистрация':
    from code_1 import register
    register()
else:
    print('досвидание')