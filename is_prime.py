n = int(input())
a = n // 2
if n > 2 :
    for i in range(2,a):
        if n % i == 0:
            print('No')
	    break
    print('Yes')
elif n == 2:
    print('Yes')
elif n == 1:
    print('We have no answer to your input')
