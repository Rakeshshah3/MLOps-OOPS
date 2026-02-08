lst=[1,2,3]
string="ram"
Int_data=5
# print(type(lst))
# print(type(string))
# print(type(Int_data))

# lst.clear()
# print(lst)

# print(string.upper())

from oops_proj import chatbook
user1=chatbook()

print(user1.id)

#using static method directly from class other than object
chatbook.set_id(10)
user2=chatbook()
print(user2.id)

user3=chatbook()
print(user3.id)


# user2=chatbook()
# print(user2._chatbook__name)
# print(user2.get_name())
# user2.set_name("King")
# print(user2.get_name())
# k1=chatbook()
# k2=chatbook()
# k3=chatbook()
# print(k1.id)
# print(k2.id)
# print(k3.id)


# user1=chatbook()

# Function vs method below
# function
list=[1,2,3]
# print(len(list))

# method
# user1=chatbook()
# user1.sendmsg()