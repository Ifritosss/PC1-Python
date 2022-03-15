print("+-------------------------------------------------------+")
print("|################### SHOW DO MILHÃO ###################|")
print("+-------------------------------------------------------+")

Reais = 0
count = 1
print("ESCOLHA ENTRE: \n 1 para Começar \n 2 para Sair")

Resposta = int(input("Digite sua escolha: "))

print(">>>>Responda as perguntas com o número das alternativas!<<<<")
if Resposta == 1:
    print("\nPERGUNTA NUMERO 1")
    print("Para quantos tipos sanguíneos o tipo O+ pode doar? \n [Alternativa 1] - 2 tipos \n [Alternativa 2] - 4 tipos \n [Alternativa 3] - Todos os tipos \n [Alternativa 4] - Nenhuma dessas \n [Alternativa 5] - Apenas negativos")
    questao1 = int(input("Digite sua resposta: "))
    if questao1 == 2:
        print("Certa Resposta")
        print("O tipo sanguíneo O+ é compatível com todos os positivos, totalizando 4 tipos")
        Reais += 1
    else:
        print("Resposta errada!")
        print("O tipo sanguíneo O+ é compatível com todos os positivos, totalizando 4 tipos, a resposta correta era [Alternativa 2] - 4 tipos")
        Reais -= 1

    print("\nPERGUNTA NUMERO 2")
    print("De quem é a famosa frase: 'Penso, logo existo'? \n [Alternativa 1] - Galileu Galilei \n [Alternetiva 2] - Descartes \n [Alternativa 3] - Sócrates \n [Alternativa 4] - Platão \n [Alternativa 5] - Francis Bacon")
    questao2 = int(input("Digite sua resposta: "))
    if questao2 == 2:
        print("Certa resposta")
        print("A famosa frase 'Penso, logo existo' foi criada pelo famoso filósofo René Descartes.")
        Reais += 1
    else:
        print("Resposta errada!")
        print("René Descartes foi o responsável por essa frase, criada em base do seu pensamento de 'para quem tudo tem início na dúvida', a resposta correta era [Alternativa 2] - Descartes")
        Reais -= 1

    print("\nPERGUNTA NUMERO 3")
    print("Qual o fator que o corpo de um diabético não reproduz? \n [Alternativa 1] - Sacarose \n [Alternativa 2] - Maltose \n [Alternativa 3] - Celulose \n [Alternativa 4] - Insulina \n [Alternativa 5] - Esperma")
    questao3 = int(input("Digite sua resposta: "))
    if questao3 == 4:
        print("Certa resposta")
        print("A insulina é um hormônio que o corpo de um diabético não produz o suficiente e por isso a glicose não é metabolizada")
        Reais += 1
    else:
        print("Resposta errada!")
        print("A insulina é um hormônio que o corpo de um diabético não produz o suficiente e por isso a glicose não é metabolizada, resposta correta é [Alternativa 4] - Insulina")
        Reais -= 1

    print("\nPERGUNTA NUMERO 4")
    print("Qual país responsável pela invenção do chuveiro elétrico? \n [Alternativa 1] - França \n [Alternativa 2] - Brasil \n [Alternativa 3] - Inglaterra \n [Alternativa 4] - Austrália \n [Alternativa 5] - Itália")
    questao4 = int(input("Digite sua resposta: "))
    if questao4 == 2:
        print("Certa reposta")
        print("Francisco Canhos foi o responsável pela criação do chuveiro elétrico no Brasil, na década de 40, em Jaú-SP")
        Reais += 1
    else:
        print("Resposta errada!")
        print("O chuveiro elétrico foi criado por Francisco Canhos em São Paulo - Brasil! A resposta certa seria [Alternativa 2] - Brasil")
        Reais -= 1

    print("\nPERGUNTA NUMERO 5")
    print("É recomendado que prática ao levantar da cama? \n [Alternativa 1] - Flexão \n [Alternativa 2] - Abdominal \n [Alternativa 3] - Banho \n [Alternativa 4] - Alongamento \n [Alternativa 5] - Checar redes sociais")
    questao5 = int(input("Digite sua resposta: "))
    if questao5 == 4:
        print("Certa resposta")
        print("Ao acordar, é recomendado que façamos um alongamento, para que assim, nossos músculos possam ser preparados para a rotina do dia, por isso, é muito importante esta atividade ao acordar")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Ao acordar, é muito importante alongar seu corpo para preparar os músculos para o estímulo do dia, por isso, a resposta certa seria [Alternativa 4] - Alongamento")
        Reais -= 1

    print("\nPERGUNTA NUMERO 6")
    print("Quais o menor e o maior país do mundo respectivamente? \n [Alternativa 1] - Vaticano e Russia \n [Alternativa 2] - Nauru e China \n [Alternativa 3] - Malta e Estados Unidos \n [Alternativa 4] - São Marino e índia \n [Alternativa 5] - Mônaco e Canadá")
    questao4 = int(input("Digite sua resposta: "))
    if questao4 == 1:
        print("Certa reposta")
        print("O Vaticâno é considerado o país de menor tamanho do mundo, e o título de maior é dado para a Russia.")
        Reais += 1
    else:
        print("Resposta errada!")
        print("O Vaticâno e a Russia são, respectivamente, o menor e o maior país do mundo, então a resposta certa sera a [Alternativa 1] - Vaticano e Russia.")
        Reais -= 1

    print("\nPERGUNTA NUMERO 7")
    print("Qual o grupo em que todas as palavras foram escritas CORRETAMENTE? \n [Alternativa 1] - Asterístico, beneficiente, meteorologia, entertido \n [Alternativa 2] - Asterisco, beneficiente, metereologia, entretido \n [Alternativa 3] - Asterisco, beneficente, metereologia, entretido \n [Alternativa 4] - Asterisco, beneficente, meteorologia, entretido \n [Alternativa 5] - Asterístico, beneficiente, metereologia, entretido")
    questao5 = int(input("Digite sua resposta: "))
    if questao5 == 4:
        print("Certa resposta")
        print("Asterisco, beneficente, meteorologia, entretido estão escritas corretamente.")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Asterisco, beneficente, meteorologia, entretido estão escritas de forma correta, por isso, a resposta certa seria [Alternativa 4] - Asterisco, beneficente, meteorologia, entretido")
        Reais -= 1

    print("\nPERGUNTA NUMERO 8")
    print("Qual o personagem folclótico costuma ser agradado pelos caçadores com a oferta de fumo? \n [Alternativa 1] - Lobisomem \n [Alternativa 2] - Boitatá \n [Alternativa 3] - Caipora \n [Alternativa 4] - Saci \n [Alternativa 5] - Negrinho do Pastoreiro")
    questao5 = int(input("Digite sua resposta: "))
    if questao5 == 3:
        print("Certa resposta")
        print("Considerada a protetora da floresta, a Caipora assusta os caçadores")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Caipora é a responsável por proteger a floresta e conhecida por guiar os caçadores em troca de fumo para ela, por isso, a alternativa correta seria [Alternativa 3] - Caipora")
        Reais -= 1

    print("\nPERGUNTA NUMERO 9")
    print("Como que os continentes se dividiram? \n [Alternativa 1] - Movimento das placas tectônicas \n [Alternativa 2] - Terremotos \n [Alternativa 3] - Vulcões em erupção \n [Alternativa 4] - Meteoros \n [Alternativa 5] - Desabamento de montanhas")
    questao5 = int(input("Digite sua resposta: "))
    if questao5 == 1:
        print("Certa resposta")
        print("Por causa dos movimentos das placas tectônicas, os continentes que antes eram bem unidos começaram a se transformar no que conhecemos hoje, por isso, a resposta correta é a [Alternativa 1] - Movimento das placas tectônicas")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Por causa dos movimentos das placas tectônicas, os continentes que antes eram bem unidos começaram a se transformar no que conhecemos hoje, por isso, a resposta correta seria [Alternativa 1] - Movimento das placas tectônicas")
        Reais -= 1

    print("\nPERGUNTA NUMERO 10")
    print("Quantos graus um ser humano consegue suportar de calor e frio, respectivamente. \n [Alternativa 1] - 125°C e -28°C \n [Alternativa 2] - 127°C e -28°C \n [Alternativa 3] - 127°C e -29°C \n [Alternativa 4] - 125°C e -29°C \n [Alternativa 5] - 110°C e 20°C")
    questao5 = int(input("Digite sua resposta: "))
    if questao5 == 3:
        print("Certa resposta")
        print("Por mais que seja por pouco tempo, um ser humano é capaz de suportar de 127°C de calor e -29°C de frio, sendo assim, [Alternativa 3] - 127°C e -29°C")
        Reais += 1
    else:
        print("Resposta errada!")
        print("O ser humano consegue suportar 127°C de calor e -29°C de frio por poucos minutos, a resposta correta seria [Alternativa 3] - 127°C e -29°C")
        Reais -= 1
        
    print("\nPARABÉNS! Você conseguiu um total de R$ %1.6f" % (Reais))
    print("\nObrigado por jogar o nosso jogo! Aperte qualquer tecla para encerrar a janela! <3")
else:
    print("Até logo!")