d = {}
file_in = open('in.txt', 'r', encoding='utf-8')
for line in file_in:
    line = line.split()
    name, num = line[0], line[2]
    if name in d:
        d[name].append(num)
    else:
        d[name] = [num]
file_in.close()

file_out = open('out.txt', 'w', encoding='utf-8')
for name in sorted(d):
    s = [int(x) for x in d[name]]
    file_out.write(name + ': ' +
    ';'.join(d[name])+ ' = ' + str(sum(s)) + '\n')
file_out.close()
