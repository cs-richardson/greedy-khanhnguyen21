#Loop
while(1):
    money = int(round(float(input('How much change is owed?')), 2)*100)
#Check negative
    if money < 0:
        print('Please enter a valid number')
#Calculations
    else:
        bill25 = int(money // 25)
        money = money % 25
        bill10 = int(money // 10)
        money = money % 10
        bill5 = int(money // 5)
        money = money % 5
        bill1 = int(money // 1)
        totalCoin =  bill25 + bill10 + bill5 + bill1
        print('You need a total amount of ',totalCoin,' coins')
        #print(bill25, 'quarters ', bill10,' dimes ', bill5,' nickels ', bill1,' pennies ')
#Check for continuation
        if input('Continue? y/n') == 'n':
            break
        
