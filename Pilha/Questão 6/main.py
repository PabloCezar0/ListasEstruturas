from pilha import Stack



pilhaIn = Stack()
pilhaOut = Stack()
manobras = 0
found = 0

selection = 1

while selection != 0:
    print("\n\n\n1. Entrada de carro\n2. Saida de carro\n\n\n 0. Exit")
    selection = int(input("Faca sua escolha: "))


    if selection == 0:
        print("\n\nObrigado por usar nossos servicos!\n\n")

    if selection == 1 and len(pilhaIn) < 10:
        carro = str(input("Digite a placa de seu carro: "))
        pilhaIn.push(carro)
        if len(pilhaIn) == 10:
            print("Estacionamento cheio")

    if selection == 1 and len(pilhaIn) == 10:
        print("Estacionamento cheio, sentimos muito!")

    if(selection == 2 and len(pilhaIn) > 0):
        carro = str(input("Digite a placa de seu carro: "))

        if pilhaIn.top.data != carro  :
            print("Teste1")
            while len(pilhaIn) > 0 and pilhaIn.top.data != carro: 
                
                pilhaOut.push(pilhaIn.pop())
                manobras += 1

            if len(pilhaIn) > 0:
                    found = 1
            else:
                found = 0
                manobras = 0

        if  found == 0 :
            print("Carro nao encontrado")
            while len(pilhaOut) > 0:
                pilhaIn.push(pilhaOut.pop())

        if found == 1:
            print("Tirando o carro: ", pilhaIn.pop())
            
            while len(pilhaOut) > 0:
                pilhaIn.push(pilhaOut.pop())
            print(pilhaIn.top.data)     
            print("O carro ",carro," manobrou ", manobras," vezes para sair do estacionamento")
            manobras = 0   

        

    print("Quantidade de carros no estacionamento : ", len(pilhaIn))
    
    
