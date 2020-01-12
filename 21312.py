import random
print("Введите имя")
name = input()
tn = "Nikita"
K =["Ты лучший","Молодец","Крутой","Красаучиг","Ты просто ты"]
SK =["Ты самый лучший","ВАХ КРАСАУЧИГ","Самый самый крутой","Самый молодец"]
if name == tn:
    print(random.choice(SK))
else:
    print(random.choice(K))
