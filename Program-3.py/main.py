a=int(input("Enter a number:").strip())

n=a if a%2==1 else a-1

if n<=0:
    print("")
else:
    odds=[str(2*i-1) for i in range(1,n + 1)]
    print(", ".join(odds))