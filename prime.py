lower=int(input("please enter the lower range"))
upper=int(input("please enter the upper range"))
num=0
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break 
        else:
            print(num)