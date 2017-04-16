N = int(raw_input("How many floors do you want? "))
for i in range(1, N+1):
    print " "*(N-i)+"*"*((2*i)-1)
    
