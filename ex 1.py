notas = []
cont_aux = 0
N = 1
Q = 0
#N is the number of keys and Q is the quantity of chords
while (N < 2 or N > 100000 or Q < 1 or Q > 100000):
    input1, input2 = input().split()
    N = int(input1)
    Q = int(input2)

#Generate an array with the integer 1 in each spot
for i in range(0, N):
    notas.append(1)

#Routine capable of reading an interval
for i in range(0, Q):
    input1, input2 = input().split()
    #Routine responsible for establish the numbers frequency
    for j in range(int(input1), int(input2)+1):
        cont = 0
        aux = notas[j]
        for k in range(int(input1), int(input2)+1):
            if(aux == notas[k]):
                cont += 1
        if(cont > cont_aux):
            cont_aux = cont
            freq = aux
        elif (cont == cont_aux):    #If there's more than a number with the highest frenquency, the highest number will have the preference
            if(aux > freq):
                freq = aux

    #Algorithm described by the exercise
    for j in range(int(input1), int(input2)+1):
        notas[j] = (notas[j]+freq)%9
    cont_aux = 0

#Shows the final array
for i in range(0, N):
    print(notas[i])

