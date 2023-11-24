import random

dig=['0','1','2','3','4','5','6','7','8','9']

low=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

up=['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbol=['!','@','#','$','%','=',':','?','.','/','|','~','>','<','(',')']

while(1):
    print("1.Create password using your name\n2.Create a random strong password\n3.Check the strength of any password\n4.Exit\n")
    ch=int(input("Enter your choice: "))
    if ch == 1:
        name=input("Enter your full name without space: ")
        len=int(input("\nEnter the length of the password: "))
        split_ch = []
        for i in name:
            split_ch.append(i)
        n_total=dig+symbol
        n_str="".join(split_ch[0:3])
        n_pass=""
        for x in range(len-3):
            n_pass=n_pass+random.choice(n_total)
        n_password="".join(split_ch[0:3])
        for x in n_pass:
            n_password=n_password+x 
        print("The password is: ",n_password)

    elif ch == 2:
        len=int(input("\nEnter the length of the password: "))
        total=dig+low+up+symbol
        r_dig=random.choice(dig)
        r_up=random.choice(up)
        r_low=random.choice(low)
        r_symbol=random.choice(symbol)
        temp_pass=r_dig+r_up+r_low+r_symbol

        for x in range(len-4):
            temp_pass=temp_pass+random.choice(total)
        password=""
        for x in temp_pass:
            password=password+x
        print("The password is: ",password)
    elif ch == 3:
        check=input("Enter the password you want to check: ")
        len_criteria=8
        low_criteria=1
        low_c=0
        for char in check:
            for x in low:
                if char == x:
                    low_c=low_c+1
        up_criteria=1
        up_c=0
        for char in check:
            for x in up:
                if char == x:
                    up_c=up_c+1
        dig_criteria=1
        dig_c=0
        for char in check:
            for x in dig:
                if char == x:
                    dig_c=dig_c+1
        symbol_criteria=2
        sym_c=0
        for char in check:
            for x in symbol:
                if char == x:
                    sym_c=sym_c+1
        flag=0
        if(len(check)<len_criteria):
            print("Password should be at least 8 characters long.")
            flag=1
        else:
            if(low_c<low_criteria):
                print("Password should contain at least 1 lowercase character.")
                flag=1
            if(up_c<up_criteria):
                print("Password should contain at least 1 uppercase character.")
                flag=1
            if(dig_c<dig_criteria):
                print("Password should contain at least 1 numerical character.")
                flag=1
            if(sym_c<symbol_criteria):
                print("Password should contain at least 1 special character.")
                flag=1
        if(flag==1):
            print("\nPassword is weak.")
        else:
            print("Password is strong.")
    elif(ch==4):
        print("Exit")
        break
    else:
        print("Invalid Choice")
