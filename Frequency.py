#To find the frequency of words in a given string
def repeat(s):
    a=s.split(" ")
    d=dict.fromkeys(a)
    #logic to print the frequency..
    for i in d:
        d[i] = 0
        for j in a:
            if i == j:
                d[i] = d[i] + 1
    print(d)









k = input("enter")
repeat(k)