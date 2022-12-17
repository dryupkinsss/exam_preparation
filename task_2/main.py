d = {}
with open('in.txt', 'r', encoding='utf-8') as file_in:
    for line in file_in:
        line = line.split()
        names, books = line[1], int(line[2])
        if names in d:
            d[names] += books
        else:
            d[names] = books

with open('out.txt', 'w', encoding='utf-8') as file_out:
    for names in sorted(d):
        file_out.write(names + ' ' + str(d[names]) + '\n')
