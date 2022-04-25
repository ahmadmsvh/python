# some comments.
import random
#any suggestion?
rand_one = random.randint(5,12)
rand_two = random.randint(5,12)

remain_one = rand_one
remain_two = rand_two

while remain_one + remain_two > 0 :
    #this loop is for ilustrating of ramaining matches
    print("First Row: ")
    for i in range(1 , remain_one + 1):
        print("|" , end="\t")
        
    print("\n")
    
    print("Second Row:")
    for i in range(1 , remain_two + 1):
        print("|", end="\t")
    
    print("\n")
    
    wrong_input = True
    # while wrong_input == True:
    #     choice = 0    
    #     while choice < 1 or choice > 3:
    #         choice = int(input("enter '1' for first row, '2' for second row ,or 3 for both:\t"))
    #     user_input = int(input("enter number of mactches to remove:\t"))
    #     if choice == 1: 
    #         if user_input <= remain_one:
    #             wrong_input = False
    #             remain_one = remain_one - user_input
    #     elif choice == 2 :
    #         if user_input <= remain_two:
    #             wrong_input = False
    #             remain_two = remain_two - user_input
    #     else:
    #         if user_input <= remain_one and user_input <= remain_two :
    #             wrong_input = False
    #             remain_one = remain_one - user_input
    #             remain_two = remain_two - user_input
            
     
print("you are winner")
