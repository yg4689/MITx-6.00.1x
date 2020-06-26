# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print


temp=s[0]
temp2=""
n=0
while n+1 <len(s):
    if s[n+1]>=s[n]:
        temp+=s[n+1]
        n=n+1
    else:
        if len(temp)>len(temp2):
            temp2=temp
            temp=""
        n=n+1
        temp=s[n]

if len(temp)>len(temp2):
    print(temp)
else:
    print(temp2)