ENTREVISTADOS = 10

qtd_excelente = 0
qtd_ruim = 0

print("-" * 40)
print("   PESQUISA DE SATISFAÇÃO -")
print("-" * 40)

for i in range(ENTREVISTADOS):
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Opções de opinião:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = 0
    while opiniao not in [1, 2, 3]:
        opiniao = int(input("Digite a sua opinião sobre o atendimento (1, 2 ou 3): "))
        if opiniao not in [1, 2, 3]:
            print("Opção inválida! Tente novamente.")

    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1
  
print("\n" + "=" * 40)
print("          RESULTADO DA PESQUISA")
print("=" * 40)
print(f") Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f") Quantidade de respostas RUIM: {qtd_ruim}")
