pedido = 0
quantidade = 0
total = 0.0
pt = []

print('\nOlá, Seja Bem vindo\n\nEste é nosso cardápio, siga as instruções para realização do seu pedido.\n\nLembrando que o pagamento será feito na entrega do pedido! :-)\n' )
print('\nMENU\n 1 - X-Salada - R$10.00 \n 2 - X-Burguer - R$10.00 \n 3 - X-Egg - R$12.00 \n 4 - X-Bacon - R$12.00 \n 5 - X-Tudo - R$15.00 \n 6 - Hot-Dog Simples - R$6.00 \n 7 - Coca-Cola - R$5.00 \n 8 - Fanta Laranja - R$5.00 \n 9 - Guaraná - R$5.00\n 10 - Suco Natural - R$7.00\n')
print('Selecione uma das opções para iniciar o seu atendimento!\n1 - Para realizar o seu pedido\n2 - Para adicionar mais itens\n3 - Para vizualizar o cardápio novamente\n4 - Para finalizar o pedido ')
resposta = int(input('\n\nDigite uma das opções!\n'))

while resposta != 0:

    if resposta == 1 or resposta == 2:
        pedido = (int(input('Primeiro digite o número do item: \n ')))
        quantidade = (int(input('Agora digite a quantidade que deseja deste item: \n')))
        resposta = (int(input('Escolhas umas das opções:\n2 - Para adicionar mais itens\n3 - Para vizualizar o cardápio novamente \n4 - Para finalizar o pedido!\n')))
        if pedido == 1 :
            td = 10.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} X-Salada | Valor: R$10.00 | Valor total: R${td}')

        elif pedido == 2:
            td = 10.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} X-Burguer | Valor: R$10.00 |Valor total: R${td}')

        elif pedido == 3:
            td = 12.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} X-Egg | Valor: R$12.00 | Valor total: R${td}')

        elif pedido == 4:
            td = 12.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} X-Bacon | Valor: R$12.00 | Valor total: R${td}')

        elif pedido == 5:
            td = 15.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} X-Tudo | Valor: R$15.00 | Valor total: R${td}')

        elif pedido == 6:
            td = 6.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} X-Hot-dog Simples | Valor: R$6.00 | Valor total: R${td}')

        elif pedido == 7:
            td = 5.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} Coca-Cola | Valor: R$5.00 | Valor total: R${td}')

        elif pedido == 8:
            td = 5.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} Fanta Laranja | Valor: R$5.00 | Valor total: R${td}')

        elif pedido == 9:
            td = 5.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} Guaraná | Valor: R$5.00| Valor total: R${td}')

        elif pedido == 10:
            td = 7.00 * quantidade
            total = td + total
            pt.append(f'Você escolheu {quantidade} Suco Natural | Valor: R$7.00 |Valor total: R${td}')

        else:
            print('Opção incorreta! \nTente Novamente!\n')
            pedido = (int(input('Primeiro digite o número do item: \n ')))
            quantidade = (int(input('Agora digite a quantidade que deseja deste item: \n')))
    elif resposta == 3:
        print('\nMENU\n 1 - X-Salada - R$10.00 \n 2 - X-Burguer - R$10.00 \n 3 - X-Egg - R$12.00 \n 4 - X-Bacon - R$12.00 \n 5 - X-Tudo - R$15.00 \n 6 - Hot-Dog Simples - R$6.00 \n 7 - Coca-Cola - R$5.00 \n 8 - Fanta Laranja - R$5.00 \n 9 - Guaraná - R$5.00\n 10 - Suco Natural - R$7.00\n')
        resposta = (int(input('Digite 2 para adicionar mais itens ou 0 para finalizar!\n')))
    elif resposta == 4:
        print('\nPedido finalizado')
        resposta = (int(input('Gostaria de algo mais?\n 2 - para adicionar mais itens !\n 0 - Para finalizar o pedido\n')))
    else:
        print('Opção incorreta!\nTente Novamente\n')
        resposta = (int(input('Escolha uma das opções:\n 2 para adicionar mais itens ou 0 para finalizar!\n')))


print(*pt,sep = '\n')
print(f'O valor total do seu pedido foi de R${total}')


pagamento = int(input('\n\nQual será a forma de pagamento?\n 1 - Dinheiro\n 2 - Cartão de Débito\n 3 - Cartão de Crédito\n 4 - PIX\n '))
if pagamento == 1:
    troco = float(input('Irá precisar de troco?\n 1 - Sim\n 2 - Não\n'))
    if troco == 1:
        pd = float(input('Troco para qual valor?\n'))
        tf = pd-total
        fp = 'Dinheiro' + (f' com troco para R${pd} \nTotal do troco: R${tf}')
    elif troco == 2:
        fp = 'Dinheiro sem Troco'
    else:
        print(' Opção errada!\n Tente Novamente!\n')
        troco = float(input('Irá precisar de troco?\n 1 - Sim\n 2 - Não\n'))
elif pagamento == 2:
    fp = 'Cartão de Débito'
elif pagamento == 3:
    fp = 'Cartão de Crédito'
elif pagamento == 4:
    fp = 'PIX'
else:
    print('Opção incorreta\n Tente novamente!')
    pagamento = int(input('Qual será a forma de pagamento?\n 1 - Dinheiro\n 2 - Cartão de Débito\n 3 - Cartão de Crédito\n 4 - PIX\n '))

endereco = str(input('Digite o endereço de entrega: \n(Rua Nª 123, Bairro, CEP)\n'))


print('\n',*pt,sep = '\n')
print(f'\nO valor total do seu pedido foi de R${total}')
print(f'A opção de pagamento ecolhida foi: {fp}')
print(f'Sera entregue no endereço: {endereco}')
print(f'Seu pedido chega entre 30 a 40 minutos\nObrigada pela preferência :-) ')






