def inverte_string(string:str):
    for i in range (len(string)-1,-1,-1):
        print(string[i],end="")
    print("")
inverte_string('abacate')
