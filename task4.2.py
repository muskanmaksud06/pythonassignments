file1=open("output.txt","w")
writing_file=file1.write("Hello, Python!")
file1.close()

file2=open("output.txt","a")
appending_file=file2.write("\nLearning file handling in Python.")
file2.close()

file3=open("output.txt","r")
reading_file=file3.read()
print(reading_file)
file3.close()