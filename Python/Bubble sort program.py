def bubblesort(a):
    n=len(a)
    for i in range(1,n):
        for j in range(n-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print("List after bubble sorting",a)
  
n=input("Enter comma separated values eg. 1,2,3 :")
a=list(eval(n))
print("List before sorting:",a)
bubblesort(a)
