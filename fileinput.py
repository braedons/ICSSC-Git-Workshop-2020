def read():
    result = []

    while (True):
        text = input()

        if (text == ""):
            break
        else:
            result.append(text + "\n")

    return result
