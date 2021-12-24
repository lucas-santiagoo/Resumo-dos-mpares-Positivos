nums = input().split()
print("Resumo dos Ímpares Positivos")
print()
cont = ""
soma = 0
for l in nums:
    numero = int(l)
    if l % "2" != "0"and l > "0":
           soma += numero
           cont += nums[l]
           quant = len(cont) 
           if quant == 0:
                print(f"Quantidade: {quant}")
                print(f"Maior: Não existe")
                print(f"menor: Não existe")
        
lista = list(cont)
maior = lista[0]
menor = lista[0]
for valor in lista:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
                
            
            

print(f"Quantidade: {quant}")        
print(f"Maior: {maior}")
print(f"Menor: {menor}")


print(soma)


