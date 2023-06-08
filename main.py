result = ""
file = open("random", "w")
for i in range(1, 307501):
    result += "\"" + str(i) + "\","
file.write(result)
file.close()
