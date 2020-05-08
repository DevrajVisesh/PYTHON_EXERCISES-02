##palindrome
#program to check the given string is palindrome.
s=input("enter")
l=len(s)
#logic..
for i in range(l//2):
    if s[i]!=s[l-i-1]:
        break
else:
    print("palindrome")