person_one = str(input("first player enter your name:\t"))
person_two = str(input("second player enter your name:\t"))

total_one_person_one =int(input("%s enter your total matches for first group:\t" %person_one))
total_two_person_one =int(input("%s enter your total matches for second group:\t" %person_one))

total_one_person_two =int(input("%s enter your total matches for first group:\t" %person_two))
total_two_person_two =int(input("%s enter your total matches for second group:\t" %person_two))

group_one = int((total_one_person_one + total_one_person_two) /2)
group_two = int((total_two_person_one + total_two_person_two) /2)

winner_flag = False
invalid_flag = False


if winner_flag == False:
    if invalid_flag == False:
        group_one_person_one = int(input("%s input your choice for group one:\t" %person_one))
        group_two_person_one = int(input("%s input your choice for group two:\t" %person_one))
        
        if group_one_person_one > 0:
            if group_two_person_one > 0:
                if group_one_person_one != group_two_person_one:
                    print("invalid \"RUN again\"")
                    invalid_flag = True

        if group_one_person_one > group_one:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if group_two_person_one > group_two:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if invalid_flag == False:
            group_one -= group_one_person_one
            group_two -= group_two_person_one

            print("group one : %d"%group_one)
            print("group two : %d"%group_two)

            if winner_flag == False:
                if group_one == 0:
                    if group_two == 0:
                        print("%s is the winner"%person_one)
                        winner_flag = True




        if group_one_person_one > 0:
            if group_two_person_one >0:
                if group_one_person_one != group_two_person_one:
                    print("invalid \"RUN again\"")
                    invalid_flag = True

        if group_one_person_one > group_one:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if group_two_person_one > group_two:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if invalid_flag == False:
            group_one -= group_one_person_one
            group_two -= group_two_person_one

            print("group one : %d"%group_one)
            print("group two : %d"%group_two)

            if winner_flag == False:
                if group_one == 0:
                    if group_two == 0:
                        print("%s is the winner"%person_one)
                        winner_flag = True



if winner_flag == False:
    if invalid_flag == False:
        group_one_person_two = int(input("%s input your choice for group one:\t" %person_two))
        group_two_person_two = int(input("%s input your choice for group two:\t" %person_two))

        if group_one_person_two > 0:
            if group_two_person_two >0:
                if group_one_person_two != group_two_person_two:
                    print("invalid \"RUN again\"")
                    invalid_flag = True

        if group_one_person_two > group_one:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if group_two_person_two > group_two:
            print("invalid \"RUN again\"")
            invalid_flag = True

        if invalid_flag == False:
            group_one -= group_one_person_two
            group_two -= group_two_person_two

            print("group one : %d"%group_one)
            print("group two : %d"%group_two)

            if winner_flag == False:
                if group_one == 0:
                    if group_two == 0:
                        print("%s is the winner"%person_two)
                        winner_flag = True


if winner_flag == False:
    if invalid_flag == False:
        group_one_person_one = int(input("%s input your choice for group one:\t" %person_one))
        group_two_person_one = int(input("%s input your choice for group two:\t" %person_one))
        
        if group_one_person_one > 0:
            if group_two_person_one >0:
                if group_one_person_one != group_two_person_one:
                    print("invalid \"RUN again\"")
                    invalid_flag = True

        if group_one_person_one > group_one:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if group_two_person_one > group_two:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if invalid_flag == False:
            group_one -= group_one_person_one
            group_two -= group_two_person_one

            print("group one : %d"%group_one)
            print("group two : %d"%group_two)

            if winner_flag == False:
                if group_one == 0:
                    if group_two == 0:
                        print("%s is the winner"%person_one)
                        winner_flag = True



if winner_flag == False:
    if invalid_flag == False:
        group_one_person_two = int(input("%s input your choice for group one:\t" %person_two))
        group_two_person_two = int(input("%s input your choice for group two:\t" %person_two))

        if group_one_person_two > 0:
            if group_two_person_two >0:
                if group_one_person_two != group_two_person_two:
                    print("invalid \"RUN again\"")
                    invalid_flag = True

        if group_one_person_two > group_one:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if group_two_person_two > group_two:
            print("invalid \"RUN again\"")
            invalid_flag = True

        if invalid_flag == False:
            group_one -= group_one_person_two
            group_two -= group_two_person_two

            print("group one : %d"%group_one)
            print("group two : %d"%group_two)

            if winner_flag == False:
                if group_one == 0:
                    if group_two == 0:
                        print("%s is the winner"%person_two)
                        winner_flag = True



if winner_flag == False:
    if invalid_flag == False:
        group_one_person_one = int(input("%s input your choice for group one:\t" %person_one))
        group_two_person_one = int(input("%s input your choice for group two:\t" %person_one))
        
        if group_one_person_one > 0:
            if group_two_person_one >0:
                if group_one_person_one != group_two_person_one:
                    print("invalid \"RUN again\"")
                    invalid_flag = True

        if group_one_person_one > group_one:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if group_two_person_one > group_two:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if invalid_flag == False:
            group_one -= group_one_person_one
            group_two -= group_two_person_one

            print("group one : %d"%group_one)
            print("group two : %d"%group_two)

            if winner_flag == False:
                if group_one == 0:
                    if group_two == 0:
                        print("%s is the winner"%person_one)
                        winner_flag = True



if winner_flag == False:
    if invalid_flag == False:
        group_one_person_two = int(input("%s input your choice for group one:\t" %person_two))
        group_two_person_two = int(input("%s input your choice for group two:\t" %person_two))

        if group_one_person_two > 0:
            if group_two_person_two >0:
                if group_one_person_two != group_two_person_two:
                    print("invalid \"RUN again\"")
                    invalid_flag = True

        if group_one_person_two > group_one:
            print("invalid \"RUN again\"")
            invalid_flag = True
        
        if group_two_person_two > group_two:
            print("invalid \"RUN again\"")
            invalid_flag = True

        if invalid_flag == False:
            group_one -= group_one_person_two
            group_two -= group_two_person_two

            print("group one : %d"%group_one)
            print("group two : %d"%group_two)

            if winner_flag == False:
                if group_one == 0:
                    if group_two == 0:
                        print("%s is the winner"%person_two)
                        winner_flag = True