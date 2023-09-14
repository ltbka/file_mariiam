
def register():
    with open('logins.txt','w')as file :
        global add
        login = input('Введите свой логин: ')
        password = input('Введите свой пароль : ')
        file.write(login + ' ' + password +'\n')
    with open('logins.txt', 'r') as file:
        add = file.readline()
        add = add.replace('\n' , '')
        add = add.split()
        print(add)
def login():
    logins = input('Введите логин')
    passw = input('Введите пароль')
    if logins == add[0] and passw == add[1]:
        print('Успешно')
    elif logins == add[0] and passw != add[1]:
        print('не правельный пароль')
    elif logins != add[0]:
        print('Не правельный логин')
    