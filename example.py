def calc(data, mode, u):
    r = []
    for i in range(len(data)):
        if data[i]["status"] == "active":
            if mode == "sum":
                r.append(data[i]["value"])
            else:
                if data[i]["value"] > 0:
                    r.append(data[i]["value"] * 1.1)
                else:
                    print("skip")
    total = 0
    for x in r:
        total = total + x
    if u != None and u == True:
        total = total - (total * 0.05)
    try:
        f = open("log.txt", "a")
        f.write(str(total) + "\n")
        f.close()
    except:
        pass
    return total