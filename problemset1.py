#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

count=0
for char in s:
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        count+=1
print("Number of vowels: "+str(count))