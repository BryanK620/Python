#not -> não -> negação (serve para negar um resultado lógico ou o resultado de uma expressão booleana, na prática, isso significa que o resultado de uma expressão será invertido)
#Ex: V (true, false) not V(false, true)

x = True
y = False
print(not x)
print(not y)
#and -> e -> conjunção
#Este operador irá prover um resultado verdadeiro se, e somente se, ambas entradas forem verdadeiras
#Ex: V1(false, false, true, true) V2(false, true, false, true)-> V1 and V2 (false, false, false, true)

x = False
y = True
print(x and y)

#or -> ou -> disjunção
#Este operador irá prover um resultado verdadeiro se ao menos uma das entradas for verdadeira
#Ex: V1(false,false,true,true) V2(false,true,false,true) -> V1 or V2 (false, true, true, true)

x = False
y = False
print(x or y)