# def Sum_All_Numbers(*Numbers) :
#     print(Numbers)
#     total = 0
#     for Num in Numbers :
#         total += Num
#     return total

# Numbers = [1,2,3,4,5,6]

# print(Sum_All_Numbers(Numbers)) => ([1,2,3,4,5,6],)
# print(Sum_All_Numbers(*Numbers)) # => 21
# print(Sum_All_Numbers(1 , 2 , 3 , 4))
# print(Sum_All_Numbers(4 , 6))


# def Show_User_Info (**KeywordArgs) :
#     for key , value in KeywordArgs.items():
#         print(f"{key} : {value}")
#     print(KeywordArgs)

# Show_User_Info(Name = "Shadmehr" , Family = "Malawaiseh" , Age = 19)
# Show_User_Info(Name = "Shadmehr" , Family = "Malawaiseh" , Age = 19 , Email = "On8802769@gmail.com")

# # Parametrs
# # *args
# # Defualt parametrs
# # **kwargs

# def Display_Info(a,b,*args, defpara = "Defualt" , **kwargs) :
#     return[a,b,args, defpara , kwargs]

# print(Display_Info(1,2,6,First_Name = "Shadmehr" , Family = "Malawaiseh"))


def Show_Names(Name, Family):
    print(f"Name is {Name} and Family is {Family}")


Person = {"Name": "Sara", "Family": "Moradi"}

Show_Names(**Person)  # ** => برای بیرون کشیدن ولیو ها استفاده میشود
