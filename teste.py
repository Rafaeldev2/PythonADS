escolha = 5
sacola = []
precos = {
    1: 5.00,   # BANANA
    2: 3.00,   # MAÇÃ
    3: 4.00,   # BERGAMOTA
    4: 5.00,   # UVA
    5: 2.50,   # PÃO
    6: 7.00,   # LEITE
    7: 6.90,   # MEL
    8: 10.00,  # SALAME
    9: 9.50,   # QUEIJO
    10: 8.50   # PRESUNTO
}

while True:
    print("""
            ============ MENU ===============
        
        Olá, seja bem vindo ao mercadinho Seu Zé

         (Por favor, digite apenas números: )

        1- Começar uma compra
        
        2- Ir para o carrinho

        3- Sair
        
        """)
    
    while True:                
        try:         
            x = int(input("Digite aqui: "))
            
            if x == 1 or x == 2 or x == 3:
                break            
            else:
                print("Opção inválida, por favor tente novamente")
        except ValueError:
            print("Opção inválida, por favor tente novamente")

    if x == 1:  # MENU do cliente
        while True:
            print("""
                ============ LISTA DE PRODUTOS ===============
            
            Olá cliente, o que deseja?

           
            Digite o ID do produto que deseja comprar
                  
                  01 - BANANA: R$ 5.00
                  02 - MAÇÃ: R$ 3.00
                  03 - BERGAMOTA: R$ 4.00
                  04 - UVA: R$ 5.00
                  05 - PÃO: R$ 2.50
                  06 - LEITE: R$ 7.00
                  07 - MEL: R$ 6.90
                  08 - SALAME: R$ 10.00
                  09 - QUEIJO: R$ 9.50
                  10 - PRESUNTO: R$ 8.50

                  Digite voltar digite '0'

            """)
            while True:
                try:
                    produto_id = int(input("Escolha o ID do produto: "))
                    
                    if produto_id == 0:
                        break
                    elif produto_id <= 10 and produto_id >= 1:
                        quantidade = int(input("Escolha a quantidade do produto: "))
                    else:
                        print("Opção inválida, por favor tente novamente")
                    preco_total = precos[produto_id] * quantidade
                    sacola.append([produto_id, quantidade, preco_total])
                except ValueError:
                    print("Opção inválida, por favor tente novamente")
            if produto_id == 0 or quantidade == 0:
                break

            

    if x == 2:  # MENU do carrinho
        while True:
            print("""
                ============ CARRINHO ===============
            
            Olá colaborador, o que deseja?

            1- Verificar itens da compra

            2- Continuar comprando

            3- Pagar e sair

            """)

            contador = 0
            total_compra = 0
            for produto in sacola:
                if len(sacola) == 0:
                    break
                else:
                    print(contador, "#", produto[0], " - Quantidade:", produto[1], " - Preço total:", produto[2])
                    total_compra += produto[2]
                    contador += 1
                    print("Preço final da compra:", total_compra)

            while True:
                try:
                    xf = int(input("Digite aqui: "))

                    if xf == 1 or xf == 2 or xf == 3:
                        break
                    else:
                        print("Opção inválida, por favor tente novamente")
                except ValueError:
                    print("Opção inválida, por favor tente novamente")
            
            if xf == 3:  # Verificação do cartão de débito
                senha_correta = input("Digite a senha do cartão de débito: ")
                tentativas = 3
                while tentativas > 0:
                    senha = input("Digite a senha novamente para confirmar: ")
                    if senha == senha_correta:
                        print("Pagamento efetuado com sucesso!")
                        break
                    else:
                        tentativas -= 1
                        if tentativas > 0:
                            print("Senha incorreta! Tentativas restantes:", tentativas)
                        else:
                            print("Cartão bloqueado! Fim do programa.")
                            exit()
                break

    if x == 3:  # Esse if é para sair do programa
        break