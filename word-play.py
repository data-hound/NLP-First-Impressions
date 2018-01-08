def ex97():
    fin=open('words.txt')
    flag=False
    word2=[]
    for line in fin:
        word=line.strip()
        #char=list(256)
        
        for i in range (0,len(word)-6):
            if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
                word2.append(word)
                print(word)
                flag=True
    print (word2)
    return flag

def ex98():
    for i in range(100000,1000000):
        i1=i%10000
        if isPallindrome(i1):
            i2=(i+1)%100000
            if isPallindrome(i2):
                i3=i+2
                i31=(i3%100000)/10000
                if isPallindrome(i31):
                    i4=i+3
                    if isPallindrome(i4):
                        print(i)

def isPallindrome(num):
    n=num
    temp=0
    while (0<n):
        rem=n%10
        temp=(temp*10)+rem
        n=n/10
    print (temp)
    print (num)
    return (temp==num)
        
        
            
            
                
