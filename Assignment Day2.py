#Delete all occurrences of an element in a list
list = [1,2,3,4,1,5,1]
repeated_ele =1

#remove the item for all its occurrences
for item in list:
	if(item==repeated_ele):
		list.remove(repeated_ele)

print(list)


#Check whether a string is a pangram.
def check_pangram(arg):
  if len(set('abcdefghijklmnopqrstuvwxyz') - set(arg.lower())) == 0 :
    return True

  return False

user_str = input("Enter a string to check for pangram : ")

if(check_pangram(user_str)):
  print("It is a pangram string")
else:
  print("Not a pangram string")





#OTP Generation Project
import  random as r
import string as str
len = 6
otp = ''
char = str.ascii_letters + str.digits#getting all alpha+digits

for i in range(len):
    otp = otp +r.choice(char)

print("OTP: ", otp)
