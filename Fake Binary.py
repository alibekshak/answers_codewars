def fake_bin(x):
    bin = ""
    for i in x:
        if int(i) < 5:
            bin += "0"
        else:
            bin += "1" 
    return bin 