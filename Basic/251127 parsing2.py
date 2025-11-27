txt = 'BBQBHCKFCMC'
var = "KFC"

for i in range(len(txt)-3):
    if var == txt[i:i+3]:
        print(i)