# parametrs

# def sum(FirstNumber):
#    return FirstNumber + 6

# print(sum(9))

# def sum(First , Second):
#     return First + Second

# print(sum(5,6))


# person = {
#     "Name" : "Shadmehr",
#     "Family" : "Malwaiseh"
# }

# def ShowfullName(FirstName , LastName):
#     return FirstName + " " + LastName

# print(ShowfullName(person["Name"] , person["Family"]))

# def divide(Num_1 , Num_2) :
#     return Num_1 / Num_2

# print(divide(3,5))

MyNumbers = [1,2,3,4,5,6,7] # 16

# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers :
#         if num % 2 !=0:
#             total += num
#     return total

# print(sum_odd_numbers(MyNumbers))

def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(check_even(4)) # True
print(check_even(5)) # False

