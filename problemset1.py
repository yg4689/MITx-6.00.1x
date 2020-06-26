# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
substring = "bob"
count=0
start=0
while start < len(s):
    pos = s.find(substring,start)
    if pos != -1:
        count+=1
        start=pos+1
    else:
        break
print("Number of times bob occurs is: ",count)