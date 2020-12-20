fn = "ex2.txt"
inp = open(fn).read().strip().split("\n")
inp = [x for x in inp]

result = 0
for x in inp:
    # quantas vezes aparece a letra na palavra
    vezNaPass = 0
    a = x.split()
    # a[0] aceder ao num de vezes que deve ser repetido a letra
    # a[1] aceder a letra que deve ser repetida
    # a[2] palavra onde deve estar a letra
    b = a[0].split("-")
    # b[0] b[1] aceder cada um dos valores
    c = a[1].split(":")
    # c[0] aceder a letra sem os 2 pontos
    
    h = [x for x in a[2]]
    if h[int(b[0])-1] == c[0]:
        jaExiste = True
        if not (h[int(b[1])-1] == c[0]):
            result += 1
    if h[int(b[1])-1] == c[0] and not (h[int(b[0])-1] == c[0]):
            result += 1

print(result)