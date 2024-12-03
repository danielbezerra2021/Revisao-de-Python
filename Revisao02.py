# sourcery skip: switch
n = int(input("Digite um numero: "))

if n%2 == 0:
    print("Esse numero é par!")
else:
    print("esse numero é  impar!")

#=======================================#
for i in range(1, 21):
    if i == 3:
        continue
    elif i == 6:
        continue
    elif i == 9:
        continue
    elif i == 12:
        continue
    elif i == 15:
        continue
    elif i == 18:
        continue
    print(i)