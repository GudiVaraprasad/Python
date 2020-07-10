def guest_list(guests):
    for i in guests:
        name,age,job=i
        print("{} is {} years old and works as {}".format(name,age,job))
        
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
