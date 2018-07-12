#to calculate quartiles
def median(nums):
    if len(nums)%2 == 0:
        return int(sum(nums[len(nums)//2-1:len(nums)//2+1])/2)
    else:
        return nums[len(nums)//2]

def quartiles(N,nums):
    Q1 = median(nums[:len(nums)//2])
    Q2 = median(nums)
    if N%2 == 0:
        Q3 = median(nums[len(nums)//2:])
    else:
        Q3 = median(nums[len(nums)//2+1:])
    return Q1,Q2,Q3

N = int(input())
nums = sorted([int(num) for num in input().split()])
Q1,Q2,Q3 = quartiles(N,nums)
print(Q1)
print(Q2)
print(Q3)

#interquartile range
#The interquartile range of an array is the difference between its first () and third () quartiles.
print(float(abs(Q1-Q3)))

#to find standard deviation
n=int(input())
sum=0
b=[]
l=([int(a) for a in input().split()])
for i in l:
    sum=sum+i
mean=sum/n
for i in l:
    j=(i-mean)**2
    b.append(j)
sum=0
for i in b:
    sum=sum+i
mean=sum/n
deviation=(mean)**(1/2)
print(round(deviation,1))
