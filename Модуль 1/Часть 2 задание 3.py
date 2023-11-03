running = True
while running:
    Password = str(input('Введите ваш пароль : '))
    if len(Password) >= int(9) :
        print('Ваш пароль принят!')
        running = False
    else : 
        print('В вашем пароле должно быть больше 8-ми символов')
