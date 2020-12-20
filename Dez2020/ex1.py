#adventOfCode day 1


fn = "ex1In.txt"
inp = open(fn).read().strip().split("\n")
print(inp)
a = [int(x) for x in inp] # passar cada elem para int
a.sort()
print(a)
#
# Objetivo ler input e verificar se a a soma de 2 num dah 2020 e saber 
# qual a multiplicação entre eles

for x in a:
    for y in a:
        for z in a:
            if(x+y+z == 2020):
                print(int(x)*int(y)*int(z))