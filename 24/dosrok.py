s = open('dosrok.txt').readline()
s = s.replace('B', '#').replace('C','#').replace('A', '#').replace('7','*')\
    .replace('8','*').replace('9','*').replace('6','*')
while '##' in s: s = s.replace('##', '# #')
while '**' in s: s = s.replace('**', '* *')
print(max(len(c) for c in s.split()))
