# write a function that takes in a number and returns a list the length of that number but with random integers from 1 - 10000
# example: random_lst(10) should return a list with a length of 10 and all random integers -> [5,1000,90,585,5000,1002,8,5050,789,9008]
import random

def random_lst(num):
    random_lt = []
    for n in range(num):
        random_lt.append(random.randint(1,100))
    return random_lt
print(random_lst(10))


# Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.
# For example, assume the bill has the following prices:[2,4,6] . Anna declines to eat item k=bill[2] which costs 6 . If Brian calculates the bill correctly, Anna will pay (2+4)/2=3. If he includes the cost of bill[2], he will calculate (2+4+6)/2=6. In the second case, he should refund 3 to Anna.
# Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

# bonAppetit has the following parameter(s):

# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contributed to the bill

def bon_appetit(bill, k, b):
    bill.pop(k)
    total = 0
    for num in bill:
        total += num
    if total/2 == b:
        return "Bon Appetit"
    else:
        change = (b-total/2)
        return change
print(bon_appetit([72, 53, 60, 66, 90, 62, 12, 31, 36, 94],6, 288))



# Find duplicate letters in a string 

check_string = "Dermatoglypyhicss"
count = {}
for s in check_string:
    string = check_string.lower()
    if s in count:
        count[s] += 1
    else:
        count[s] = 1

for key in count:
    if count[key] > 1:
        print(key, count[key])


# Neither of these binary converters seem to work correctly the first I wrote second I found online 


# Find binary of two numbers added together 
# def binary_of_num(a,b):
#     binary = ""
#     num = a+b
#     print(num)
#     while num > 0:
#         if num % 2 != 0:
#             binary+="1"
#             num = int(num/2)
#         elif num % 2 == 0:
#             binary+="0"
#             num = int(num/2)
#         print(num%2)
#     print(binary[::-1])
# binary_of_num(9410545619407440027857948174, 3329051825520946381258672553)
# def binary_of_num(num):
#     if num >= 1:
#         binary_of_num(num//2)
#     print(num%2, end="")
# binary_of_num(9410545619407440027857948174 + 3329051825520946381258672553)
