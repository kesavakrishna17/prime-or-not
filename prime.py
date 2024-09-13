lb=int(input("Enter lower bound number:"))
up=int(input("Enter upper bound number:"))
for num in range(lb,up+1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)