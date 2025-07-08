def fibbonaci(n_terms):
    n1, n2 = 0 ,1
    count = 0
    if n_terms <= 0:
        print("Enter positive Integer")

    elif n_terms == 1:
        print("fibbonosi sequence up to",n_terms,"Item:")
        print(n1)
    else:
        print("fibbonaci sequence:")
        while count < n_terms:
            print(n1,end=" ")
            nth=n1 + n2
            n1=n2
            n2=nth
            count +=1

n_terms=1
fibbonaci(n_terms)



