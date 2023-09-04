#1
def soma_numeros(N, pilha=[]):
    if N == 0:
        return 0
    else:
        pilha.append(N)
        return N + soma_numeros(N - 1, pilha)

n = 5
resultado = soma_numeros(n)
print(f'A soma dos primeiros {n} números inteiros positivos é {resultado}')

#2
def fatorial(n, pilha=[]):
    if n == 0:
        return 1
    
    pilha.append(n)
    resultado = n * fatorial(n - 1, pilha)
    pilha.pop()
    
    return resultado

n = 5
resultado = fatorial(n)
print(f'O fatorial de {n} é {resultado}')


#3
def invr_string(string):
    pilha = []   
    
    for char in string:
        pilha.append(char)
 
    invercao_string = ""
    
    while pilha:
        invercao_string += pilha.pop()
    
    return invercao_string
 
string = "Programação-><-"
string_invertida = invr_string(string)
print(string_invertida)

#4
def convercao (decimal):
    pilha = []  
    
    if decimal == 0:
        pilha.append(0)
    
    while decimal > 0:
        pilha.append(decimal % 2)   
        decimal //= 2   
    
    representacao_binaria = ""
    
    while pilha:
        representacao_binaria += str(pilha.pop())
    
    return representacao_binaria

numero_decimal = 25
representacao_binaria = convercao (numero_decimal)
print(f'A representação binária de {numero_decimal} é {representacao_binaria}')
