Start=2
End=100
sm=0
for num in range(Start,End+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
            sm+=num
print("The sum of prime no is",sm) 
