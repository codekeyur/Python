# # # # # # #
# Basic function to add two values
def addition (valu1, valu2):
    value3 = value1 + value2
    return value3
    add = addition(192, 2434)
    print(add)
# # # # #
#Chekcing the Datatype of input if both are Integers then adding them.
# # # # #
def addition_operation (value1, value2):
  value1 = int(input("Please enter value-1:"))
  value2 = int(input("Please enter value-2:"))
  if type(value1) == type(value2):
      contact_string = value1 + value2
      print(contact_string)
  else:
     print("Provided values does not have same Datatype.")
  
addition_operation("Keyur", 12)