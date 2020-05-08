#To Find the longest word/string
def longest_string(s):
     a = s.split(" ")
     print(a)
     max = 0
  #To find the length of max letter word
     for i in a:
         l = len(i)
         if l > max:
             max = l
    #logic to print the max letter words
     for i in a:
         if len(i) == max:
             print(i)
k = input("enter")

longest_string(k)