print("HERE'S YOUR INTEREST")
P = 5000
t = 2
r = 8
SI = (P*t*r)/100
print('Simple interest is: %f' % (SI))

P = 5000
t = 2
r = 8
CI = P * ( (1+r/100)**t - 1)
print('Compound interest is: %f' %(CI))

while True:
    print("\nChoose 1:")
    print("1.SI")
    print("2.CI")
    print("3.Exit")
    
    choice = int(input("\nEnter Choice: "))

    if choice == 1:
        P = float(input('Enter amount: '))
        t = float(input('Enter time in years: '))
        r = float(input('Enter roi: '))
        SI = (P*t*r)/100
        print('Simple interest is: %f' % (SI))
        
        
    elif choice == 2:
        P = float(input('Enter amount: '))
        t = float(input('Enter time in years: '))
        r = float(input('Enter roi: '))
        CI = P * ( (1+r/100)**t - 1)
        print('Compound interest is: %f' %(CI))

    elif choice == 3:
        print("ThankS !")
        break
    
    else:
        print("Invalid Input!")
