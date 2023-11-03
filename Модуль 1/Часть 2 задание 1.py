a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a == b and a == c and b == c :
    print ("3")
elif a == b or a == c or b == c :
    print ("2")
else :
    print ("0")