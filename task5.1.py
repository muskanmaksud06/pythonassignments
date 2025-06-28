dictionary={"Alice":44,"Bob":55,"Charlie":66,"David":77}

user_input=input("Enter the student's name: ")
if user_input in dictionary:
     print("The marks of {} is : {}".format(user_input,dictionary[user_input]))
else:
    print("Student not found")

