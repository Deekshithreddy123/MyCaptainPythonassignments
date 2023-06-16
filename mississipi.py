def most_frequent(string):
    b= {}
    for i in string:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    sorted_frequency =sorted(b.items(),key=lambda x:x[1],reverse=True)
    for item in sorted_frequency:
        print(item[0],'=',item[1])
string ="Mississippi"
most_frequent(string)