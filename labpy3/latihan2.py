x = 1
max = 0
while x!=0 :
    if x > max :
        max = x
    x = int(input("Masukan Bilangan : "))
    if x == 0 :
        break
print("Bilangan Terbesar adalah : ",max)
