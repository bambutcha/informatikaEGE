s = open('shastin_5.txt').readline()
s = s.replace('1','*').replace('3','*').replace('5','*').replace('7','*').replace('9','*')
w = s.split('***')
m = 0
for i in range(len(w)-3):
    a = '***'.join(w[i:i+3])
    m = max(len(a),m)
print(m)

