pin = 7505
balance = 2000

guess_count = 0
guess_limit = 5
action=1

while(guess_count<=guess_limit and (action<=3 and action>=1)):
    guess_count+=1
    step1 = int(input('enter your four digit pin: '))
    if step1 == pin:
        print('congratulations! your pin has been verified. ')
        while(action<=3 and action>=1):
                print('\nChoose your action:')
                print("1 to check balance")
                print('2 to make a withdrawal')
                print('3 to pay in')
                action =int (input('\nEnter Choice: '))
                if action == 1:
                    print("your balance is rupees "+str(balance)+ " only")
                elif action == 2:
                    print('enter amount to be withdrawn')
                    amount_withdrawn = int(input('Rs. '))
                    if amount_withdrawn > balance:
                        print('oops! you dont have enough balance')
                    elif amount_withdrawn <= balance:
                        balance = balance - amount_withdrawn
                        print("your new balance is Rs. "+str(balance))
                elif action == 3:
                    print('enter amount you wish to pay in')
                    amount_paid = int(input('Rs. '))
                    balance = balance + amount_paid
                    print(" your new balance is Rs."+ str(balance))
               
    else:
        print('Wrong Password')
        
