from pilha import Stack



pilha = Stack()

expr = str(input("Digite a expressão: "))


for element in expr:
    if element == '(':
        pilha.push('(')
    
    if element == '[':
        pilha.push('[')
    
    if element == '{':
        pilha.push('{')
        
    if element == ')':
        if pilha.top.data == '(':
            pilha.pop() 

        else:
            print("Falta parentese!")
            break 
        
    if element == '}':
        if pilha.top.data == '{':
            pilha.pop() 

        else:
            print("Falta chave!")
            break 
        
    if element == ']':
        if pilha.top.data == '[':
            pilha.pop() 

        else:
            print("Falta colchete!")
            break 
        
if len(pilha) == 0:
    print("Expressão valida!")
else:
    print("Expressão invalida!")
