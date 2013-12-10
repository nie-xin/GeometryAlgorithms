man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing')

try:
    out1 = open("man_data.txt", "w")
    out2 = open("other_data.txt", "w")

    print(man, file=out1)
    print(other, file=out2)

except IOError:
    print("Can't sava to the file")

finally:
    out1.close()
    out2.close()

