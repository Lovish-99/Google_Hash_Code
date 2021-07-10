#Pizza Problem Solution!!!
#importing random library.
import random

#Declaring data types
master_list = list()
pizza_list = []
no_of_pizza = 0
two_person_team = 0
three_person_team = 0
four_person_team = 0
index = 0
max = -1
var=input("enter filename")


#Reading the given file data.
with open(var) as fh:
    for line in fh:
        index = index + 1
        temp_list = line.strip().split()
        if index == 1:
            no_of_pizza = int(temp_list[0])
            two_person_team = int(temp_list[1])
            three_person_team = int(temp_list[2])
            four_person_team = int(temp_list[3])
        else:
            pizza_list.append(temp_list[1:])
            if len(temp_list[1:])>max:
                max=len(temp_list[1:])

#Algo for the number of pizza's delivered.
total = int(two_person_team) * 2 + int(three_person_team) * 3 + int(four_person_team) * 4
if no_of_pizza < total:
    remain = total - no_of_pizza
    if remain/4 < four_person_team: 
        four_person_team = four_person_team - int(remain / 4)
        if remain % 4 == 3:
            three_person_team = three_person_team - 1
        elif remain % 4 == 2 or remain % 4 == 1:
            two_person_team = two_person_team - 1
    else:
        remain=remain-four_person_team*4
        four_person_team=0
        if remain/3 < three_person_team: 
            three_person_team = three_person_team - int(remain / 3)
            if remain%3==2 or remain%3==1 :
                two_person_team = two_person_team - 1


# Declaring and defining function for distributing pizza's for the two person team.
def two_person_pizza(two_person_tea):
    for loop in range(0, two_person_tea):
        while 1:
            pizza_index_1 = random.choice(range(0, len(pizza_list)))
            pizza_index_2 = random.choice(range(0, len(pizza_list)))
            if pizza_index_1 != pizza_index_2:
                if len(pizza_list[pizza_index_1]) > 0 and len(pizza_list[pizza_index_2]) > 0:
                    if (pizza_list[pizza_index_2] not in pizza_list[pizza_index_1] and pizza_list[pizza_index_1] not in pizza_list[pizza_index_2]) or (len(pizza_list[pizza_index_2]) < (max / 4 + 1) and len(pizza_list[pizza_index_1]) > (max / 2 + 1)):
                        print("2"," ",pizza_index_1, " ", pizza_index_2)
                        f1.writelines(("2"," ",str(pizza_index_1), " ", str(pizza_index_2),'\n'))
                        pizza_list[pizza_index_1] = []
                        pizza_list[pizza_index_2] = []
                        break


#Declaring and defining function for distributing pizza's for the three person team.
def three_person_pizza(three_person_tea):
    for loop in range(0, three_person_tea):
        pizza_index_1 = random.choice(range(0, len(pizza_list)))
        pizza_index_2 = random.choice(range(0, len(pizza_list)))
        pizza_index_3 = random.choice(range(0, len(pizza_list)))
        while 1:
            if pizza_index_1 not in [pizza_index_2,pizza_index_3] and pizza_index_2!=pizza_index_3:
                if len(pizza_list[pizza_index_1]) == 0:
                    pizza_index_1 = random.choice(range(0, len(pizza_list)))
                elif len(pizza_list[pizza_index_2]) == 0:
                    pizza_index_2 = random.choice(range(0, len(pizza_list)))
                elif len(pizza_list[pizza_index_3]) == 0:
                    pizza_index_3 = random.choice(range(0, len(pizza_list)))
                elif pizza_list[pizza_index_3] not in (pizza_list[pizza_index_1] and pizza_list[pizza_index_2]):
                    print("3"," ",pizza_index_1," ", pizza_index_2," ", pizza_index_3)
                    f1.writelines(("3"," ",str(pizza_index_1)," ", str(pizza_index_2)," ", str(pizza_index_3),'\n'))
                    pizza_list[pizza_index_1] = []
                    pizza_list[pizza_index_2] = []
                    pizza_list[pizza_index_3] = []
                    break
                else:
                    pizza_index_1 = random.choice(range(0, len(pizza_list)))
                    pizza_index_2 = random.choice(range(0, len(pizza_list)))
                    pizza_index_3 = random.choice(range(0, len(pizza_list)))


# or ( len(pizza_list[pizza_index_2]) < (max / 4) and len( pizza_list[pizza_index_1]) > (max / 2)):

#Declaring and defining function for distributing pizza's for the four person team.
def four_person_pizza(four_person_tea):
    for loop in range(0, four_person_tea):
        pizza_index_1 = random.choice(range(0, len(pizza_list)))
        pizza_index_2 = random.choice(range(0, len(pizza_list)))
        pizza_index_3 = random.choice(range(0, len(pizza_list)))
        pizza_index_4 = random.choice(range(0, len(pizza_list)))
        while 1:
            if len(pizza_list[pizza_index_1]) == 0:
                pizza_index_1 = random.choice(range(0, len(pizza_list)))
            elif len(pizza_list[pizza_index_2]) == 0:
                pizza_index_2 = random.choice(range(0, len(pizza_list)))
            elif len(pizza_list[pizza_index_3]) == 0:
                pizza_index_3 = random.choice(range(0, len(pizza_list)))
            elif len(pizza_list[pizza_index_4]) == 0:
                pizza_index_4 = random.choice(range(0, len(pizza_list)))
            elif pizza_index_1 not in [pizza_index_2,pizza_index_3,pizza_index_4] and pizza_index_2 not in [pizza_index_3,pizza_index_4] and pizza_index_3!=pizza_index_4:
                print("4"," ",pizza_index_1, " ", pizza_index_2, " ", pizza_index_3, " ", pizza_index_4)
                f1.writelines(("4"," ",str(pizza_index_1), " ", str(pizza_index_2), " ", str(pizza_index_3), " ",str(pizza_index_4),'\n'))
                pizza_list[pizza_index_1] = []
                pizza_list[pizza_index_2] = []
                pizza_list[pizza_index_3] = []
                pizza_list[pizza_index_4] = []
                break
            else:
                pizza_index_1 = random.choice(range(0, len(pizza_list)))
                pizza_index_2 = random.choice(range(0, len(pizza_list)))
                pizza_index_3 = random.choice(range(0, len(pizza_list)))
                pizza_index_4 = random.choice(range(0, len(pizza_list)))

f1= open(var+"_output.txt","w+")
f1.writelines((str(two_person_team+three_person_team+four_person_team),'\n'))
two_person_pizza(two_person_team)
three_person_pizza(three_person_team)
four_person_pizza(four_person_team)
f1.close()#Pizza Problem Solution!!!
#importing random library.
import random

#Declaring data types
master_list = list()
pizza_list = []
no_of_pizza = 0
two_person_team = 0
three_person_team = 0
four_person_team = 0
index = 0
max = -1
var=input("enter filename")
