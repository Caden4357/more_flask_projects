# DATATYPES 
# STRINGS, INTEGERS, DICTOIONARIES, LIST, TUPLE 

#complex numbers I dont understand
c = 2 + 3j
print("\nType of c: ", c)


staff = {
    "managers": [ "Michael", "John" ],
    "employees": [ "Howard", "Lori", "Elijah" ],
    "owner": [ "Bob", "Stuart" ], 
}
def printStaffInfo(staff):
    for key, val in staff.items():
        print(f"{key}")
        for items in val:
            print(f"-{items}")
printStaffInfo(staff)