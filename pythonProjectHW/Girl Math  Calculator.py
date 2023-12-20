#goal: create a basic budget calculator that allows you to input how much you want to spend
#use boolians to determine if dinner is within budget

Budget = (input("How much would you like to spend?"))
#set Budget

single_cost = (input("How much does this item cost?"))
#set the single use cost

if(single_cost > Budget):
    print("You can not afford it if you only use it once.. but.. ")
    Usage_stat = (input("How many times will you use this thing?"))
# How many times are we using the item?
    cost_per_use = (int(single_cost) / int(Usage_stat))
    print("So if you use it, " + str(Usage_stat) + " times, then it will cost " + str(cost_per_use) + " per use.")
    if(int(cost_per_use)) < int(Budget):
        print("That means you should get it!")
    if (int(cost_per_use)) > int(Budget):
        print("Yeah it isn't worth it..")




else: (print("You're golden! Go get it!"))
#If they can afford it off a single use, prompt purchase, if they can not- justify purchase.

