s= 'decimal'
a='medicat'

s_s = sorted(s)
a_s = sorted(a)
s_f = ''.join(s_s)
a_f = ''.join(a_s)
count =0

if len(s) == len(a) :
        for i in range(0,len(s)):
            if s_f[i] != a_f[i]:
                count = count+1
            if(count > 0):
                print("This is not a anagram")
                exit()

        print("This is an anagram")
else:
    print("This is not a anagram")




