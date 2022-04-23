

def edit_basicvar(filename, var, data):

    lines = []
    file = open(filename, "r")
    for line in file.read().splitlines():
        lines.append(line)
    file.close()

    open(filename, "w").close()
    file = open(filename, "a")
    for line in lines:
        if str(var) in line:
            index = lines.index(line)
            if type(data) == str:
                lines[index] = f'{var} = "{data}"'

            elif type(data) == int:
                lines[index] = f'{var} = {data}'
    for line in lines:
        file.write(line + "\n")
        file.flush()
    file.close()
    return