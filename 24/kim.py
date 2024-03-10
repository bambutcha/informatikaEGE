s = open('kim.txt').readline()
s = s.split('Y')
m = 10000
for i in range(len(s) - 100):
    c= 'Y'.join(s[i:i+101])
    m = min(m,len(c) - len(s[i]) - len(s[i+100]))
print(m)
