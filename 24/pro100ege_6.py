s = open('24.txt').readline()
w = s.split('XZZY')
m = 0
for i in range(len(w)-1200001):
    a = 'XZZY'.join(w[i:i+1200001])
    m = max(len(a),m)
print(m)
