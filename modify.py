import random
import mysql.connector
db=mysql.connector.connect(host='localhost',username='root',password='shivam2002',database='datacamp')
cursor=db.cursor()
ctr=0
bank=1


def deposit():
    money_deposit=int(input('Amount to be deposited :- '))
    print('----------------------------------')
    query='update customers set balance=balance+%s where id=%s'
    value=(money_deposit,i)
    cursor.execute(query,value)
    db.commit()
    q='select balance from customers where id=%s and username=%s'
    cursor.execute(q,(i,name))
    a=cursor.fetchall()
    a=a[0]
    for x in a:
        print('Updated Balance :- ',x)
        print('----------------------------------')


def withdraw():
    money_withdrawn=int(input('Amount to be withdrawn :- '))
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    query='update customers set balance=balance-%s where id=%s'
    value=(money_withdrawn,i)
    cursor.execute(query,value)
    db.commit()
    q='select balance from customers where id=%s and username=%s'
    cursor.execute(q,(i,name))
    a=cursor.fetchall()
    for x in a:
        print('Updated Balance :- ',x)
        print('----------------------------------')


def aadhar():
    d=int(input("Aadhar Number :- "))
    query='update customers set kyc="true" where id=%s and username=%s'
    value=(i,name)
    cursor.execute(query,value)
    db.commit()
    print("KYC Done")


def voter():
    vi=int(input("Voter Id Number :- "))
    query='update customers set kyc="true" where id=%s and username=%s'
    value=(i,name)
    cursor.execute(query,value)
    db.commit()
    print("KYC Done")


def pan():
    pc=int(input("Pan Card Number :- "))
    query='update customers set kyc="true" where id=%s and username=%s'
    value=(i,name)
    cursor.execute(query,value)
    db.commit()
    print("KYC Done")


def drive():
    dl=int(input("Driving License Number :- "))
    query='update customers set kyc="true" where id=%s and username=%s'
    value=(i,name)
    cursor.execute(query,value)
    db.commit()
    print("KYC Done")


def kyc():
    q='select kyc from customers where id=%s and username=%s'
    cursor.execute(q,(i,name))
    a=cursor.fetchall()
    a=a[0]
    for x in a:
        condition=x
    if condition=='false':
        print('Accepted Government Documents')
        print('Press 1 for Aadhar Card')
        print('Press 2 for Voter Id Card')
        print('Press 3 for Pan Card')
        print('Press 4 for Driving License')
        print('----------------------------------')
        cho=int(input('Enter your choice :- '))
        print('----------------------------------')
        if cho==1:
            aadhar()
        elif cho==2:
            voter()
        elif cho==3:
            pan()
        elif cho==4:
            drive()
        else:
            print('Invalid Choice ')
    else:
        print('KYC Already done ')
        print('----------------------------------')


def display_balance():
    q='select balance from customers where id=%s and username=%s'
    cursor.execute(q,(i,name))
    a=cursor.fetchall()
    a=a[0]
    for x in a:
        print('Balance :- ',x)
        print('----------------------------------')


def send():
    money_to_send=int(input('Amount to be sent :- '))
    ac_no=int(input('Account no of receiever  :- '))
    print('Amount sent ')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    query='update customers set balance=balance-%s where id=%s'
    value=(money_to_send,i)
    cursor.execute(query,value)
    db.commit()
    q='select balance from customers where id=%s and username=%s'
    cursor.execute(q,(i,name))
    a=cursor.fetchall()
    a=a[0]
    for x in a:
        print("Updated Balance :- ",x)
        print('----------------------------------')


def add_new_account():
    print('Fill these details to register your account ')
    idea=random.randint(6,100)
    name=input("Enter your name :- ")
    username=input('Enter your username :- ')
    pas=int(input('Enter your password :- '))
    balance=float(input('Enter your balance :- '))
    age=int(input('Enter your age :- '))
    gender=input('Enter your gender (M/F) :- ')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    kyc='false'
    query='insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s)'
    value=(idea,name,username,pas,balance,age,gender,kyc)
    cursor.execute(query,value)
    db.commit()


def delete_bank_account():
    us=input("Enter your username :- ")
    p=int(input("Enter your password :-"))
    print('----------------------------------')
    value=(us,p)
    query="select * from customers where username=%s and password=%s "
    cursor.execute(query,value)
    data_login=cursor.fetchall()
    query='delete from customers where id=%s and username=%s'
    cursor.execute(query,(data_login[0][0],data_login[0][2]))
    db.commit()


def loan_percent():
    print('Home Loan     :- 13% ')
    print('Personal Loan :- 15% ')
    print('Student  Loan :- 05% ')
    print('Car Loan      :- 11% ')
    print('----------------------------------')


def support():
    print('TollFree Number : 120090069')
    print('For Support email : boi@mail.us')
    print('----------------------------------')


def account_list():
    q='select username from customers '
    cursor.execute(q)
    a=cursor.fetchall()
    for x in a:
        print(x)
    print('----------------------------------')


while bank==1:
    print('--------------------------------------------')
    print('-----------BANK MANAGEMENT SYSTEM-----------')
    print('--------------------------------------------')
    print('Press 1 for Online Banking')
    print('Press 2 for Opening a new bank account')
    print('Press 3 for Deleting your bank account')
    print('Press 4 for displying current loan rate')
    print('Press 5 for Customer Help Services')
    print('Press 6 for displaying all account holder list')
    print('Press 7 for exit')
    print('----------------------------------')
    choice=int(input('Option :- '))
    print('----------------------------------')


    if choice==1:
        print('WELCOME TO BANK OF INDIA')
        print('----------------------------------')
        while True:
            us=input('Enter your username :- ')
            p=int(input('Enter your password :- '))
            print('----------------------------------')
            value=(us,p)
            query='select * from customers where username=%s and password=%s'
            cursor.execute(query,value)
            b=cursor.fetchall()
            if len(b)!=0:
                ctr=1
                break
            else:
                print('Username or password is wrong')
                print('Login Unsuccessful')
                print('Try Again')
                print('----------------------------------')


        if ctr==1:
            i=b[0][0]
            name=b[0][2]
            print('Login Successful')
            print('----------------------------------')
            c=1
            while c==1:
                print('Press 1 for depositing money')
                print('Press 2 for withdrawing money')
                print('Press 3 for doing kyc')
                print('Press 4 for checking balance')
                print('Press 5 for sending money by a/c no')
                print('Press 6 for logging out')
                print('----------------------------------')
                ch=int(input('Enter your choice :- '))


                if ch==1:
                    deposit()


                elif ch==2:
                    withdraw()


                elif ch==3:
                    kyc()


                elif ch==4:
                    display_balance()


                elif ch==5:
                    send()


                elif ch==6:
                    c=0


                else:
                    print('Wrong option ')
                    print('----------------------------------')


    elif choice==2:
        add_new_bank_account()


    elif choice==3:
        delete_bank_account()


    elif choice==4:
        loan_percent()


    elif choice==5:
        support()


    elif choice==6:
        account_list()


    elif choice==7:
        bank=0


    else:
        print('Wrong Option')
        print('----------------------------------')


db.close()
        
                    

                
                
                
    
    
    
    
    
        
    
        
    




    
