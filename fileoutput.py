def write(lines):
    name = "output.txt"
    f = open(name, "w+")

    for line in lines:
        f.write(lines)

    f.close()
    return name
