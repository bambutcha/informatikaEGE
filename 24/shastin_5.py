s = open('shastin_5.txt').readline()
s = s.replace('1','*').replace('3','*').replace('5','*').replace('7','*').replace('9','*')

m = [2]*len(s)

for i in range(2,len(s)):
    if s[i-2] +s[i-1]+s[i]!= '***':
        m[i] = m[i-1]+1
print(max(m))

