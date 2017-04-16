N = int(raw_input("How many floors do you want? "))
for i in range(0, N):
    print " "*(N-(1+i))+"*"*((2*i)-1)
    
