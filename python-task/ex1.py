lst=[]

for number in range(2000,3201):
    if number%7==0 and number%5!=0:
        lst.append(number)

print(lst)