turnos = 0 
entrada = 0
tripulantes = ['mulher', 'gala', 'capitao', 'soldado', 'pai', 'poker', 'mafioso', 'capanga', 'prefeito', 'quieto']

muda_capitulo = "Aperte enter para continuar..."
txt_continua = "..."

'''

    x = input(txt_continua)
    print("", end = '')
    
    
'''

def verifica_input_int(limite_inf: int, limite_sup: int, flavor_text = ""):
    '''
    Verificação de entrada
    '''
    global entrada
    entrada_correta = False
    
    while entrada_correta == False:
        try:
            entrada = int(input(flavor_text))
            while (entrada < limite_inf) or (entrada > limite_sup):
                print("Tem certeza disso? ", end = '')
                entrada = int(input(flavor_text))
            entrada_correta = True
        except:
            print("Tem certeza disso? ", end = '')

def Incremento_turno():
    global turnos
    turnos = turnos + 1

def Remover_tripulante(tripulante:str):
    global tripulantes
    tripulantes.remove(tripulante)

def Volta_saguao():
    '''
    Voltando ao menu apos conversa
    '''
    if turnos < 4:
        index = 1
        print("\nSua atenção volta ao \"hall\" e as demais figuras. Após essa convera, você decide por se aproximar de:")
        for elem in tripulantes:
            if elem == 'mulher':
                print(index, end = '')
                print(" A linda mulher do vestido vermelho.")
                index = index + 1
            elif elem == 'gala':
                print(index, end = '')
                print(" O homem charmoso que bebe whisky.")
                index = index + 1
            elif elem == 'capitao':
                print(index, end = '')
                print(" O homem com chapéu de capitão.")
                index = index + 1
            elif elem == 'soldado':
                print(index, end = '')
                print(" O homem sem o braço direito.")
                index = index + 1
            elif elem == 'pai':
                print(index, end = '')
                print(" O homem sentado que aparenta estar nervoso.")
                index = index + 1
            elif elem == 'poker':
                print(index, end = '')
                print(" homem de meia idade que mexe com cartas de baralho.")
                index = index + 1
            elif elem == 'mafioso':
                print(index, end = '')
                print(" O homem negro sentado e com vestes majestosas.")
                index = index + 1
            elif elem == 'capanga':
                print(index, end = '')
                print(" O outro homem negro que esta em pé.")
                index = index + 1
            elif elem == 'prefeito':
                print(index, end = '')
                print(" O senhor de óculos lendo um jornal.")
                index = index + 1
            elif elem == 'quieto':
                print(index, end = '')
                print(" Agora vou ficar na minha.")
                index = index + 1
        
        verifica_input_int(1, index - 1)
        
        if tripulantes[entrada - 1] == 'mulher':
            b001_Mulher()
        elif tripulantes[entrada - 1] == 'gala':
            b002_Gala()
        elif tripulantes[entrada - 1] == 'capitao':
        	b003_Capitao()
        elif tripulantes[entrada - 1] == 'soldado':
        	b004_Soldado()
        elif tripulantes[entrada - 1] == 'pai':
            b005_Pai()
        elif tripulantes[entrada - 1] == 'poker':
            b006_Poker()
        elif tripulantes[entrada - 1] == 'mafioso':
            b007_Mafioso()
        elif tripulantes[entrada - 1] == 'capanga':
            b008_Capanga()
        elif tripulantes[entrada - 1] == 'prefeito':
            b009_Prefeito()
        elif tripulantes[entrada - 1] == 'quieto':
            b010_Quieto()

    else:
        print("Sua atenção volta ao saguão, mas tanta conversa te fez perder a noção do tempo. Já é tarde e todos foram para seus aposentos. Você deve fazer o mesmo.")
        x = input(txt_continua)
    
def Intro_001():
    '''
    Introdução
    '''
    
    print("1923", end = '')
    x = input(txt_continua)

    print("Você está em um barco que zarpou há pouco. Há apenas algumas horas atrás você estava em terra firme, num porto tranquilo e desolado no meio da agitada capital, mas agora esse barco é seu chão e o mar é seu redor.", end = '')
    x = input(txt_continua)
    print("O barco é velho mas bem cuidado, e nada luxuoso, justificando o preço barato e acessível. Quanto ao tamanho, ele não é pequeno. Na verdade, ele é grande e espaçoso considerando a enxuta tripulação, da qual você lembra de ter contato mais ou menos 10 pessoas entrando no barco junto a você.", end = '')
    x = input(txt_continua)
    print("Quem são elas? De onde vieram e para onde vão? Quais suas motivações? Você não faz a mínimas a ideia, mas terá muito tempo para descobrir...\n\nA viagem, sem sombra de dúvidas, será longa.", end = '')
    x = input(txt_continua)
    print("O frio da noite e a brisa gelada te forçam a entrar no barco. Após passar por uns corredores estreitos e por umas salas, vc chega ao \"hall\" da embarcação, onde você vê os demais tripulantes. Você escolhe alguém para conversar e se aproxima de:\n")
    print("1 Uma mulher linda num vestido vermelho.")
    print("2 Um homem sem o braço direito que conversa com")
    print("3 um homem com chapéu de capitão.")
    print("4 Um homem sentado que aparenta estar nervoso.")
    print("5 Um homem de meia idade que mexe com cartas de baralho.")
    print("6 Sentado numa cadeira, um homem negro com vestes majestosas, e ao lado dele,")
    print("7 em pé, um outro homem negro igualmente bem trajado.")
    print("8 Um homem charmoso que bebe whisky no balcão.")
    print("9 Um senhor de óculos lendo um jornal.")
    print("10 Na verdade prefiro ficar quieto na minha.")
    
    verifica_input_int(1, 10, "Com quem deseja falar? ")
    
    if entrada == 1:
        b001_Mulher()
    elif entrada == 2:
        b004_Soldado()
    elif entrada == 3:
        b003_Capitao()
    elif entrada == 4:
        b005_Pai()
    elif entrada == 5:
        b006_Poker()
    elif entrada == 6:
        b007_Mafioso()
    elif entrada == 7:
        b008_Capanga()
    elif entrada == 8:
        b002_Gala()
    elif entrada == 9:
        b009_Prefeito()
    elif entrada == 10:
        b010_Quieto()
      
def b001_Mulher():
    '''
    Dialogo inicial: mulher bonita no vestido vermelho
    '''
    Incremento_turno()
    
    def c001_Mulher():
        '''
        1 Um autógrafo seu? Nem pensar!
        '''
        print("Seu sorriso se transforma em espanto. Ela te olha de cima a baixo e responde com tom de inconformidade: \"como ousa!\", e com passos firmes ela se afasta de você.")
    
    def c002_Mulher():
        '''
        2 Me desculpe mas, quem é você?
        '''
        def d001_Mulher():
            '''
            1 Hm, bom para você. Adeus
            '''
            print("Você se entedia da arrogância da mulher e se afasta")
            Remover_tripulante('mulher')
        
        def d002_Mulher():
            print("Ela gagueja um pouco antes de responder e pisca os olhos. Claramente ela não esperava uma pergunta dessas, até que responde: \"Minha agenda não lhe diz respeito, mas já que demonstrou interesse, apenas lhe direi que viajo para um país exótico onde gravarei meu próximo filme. E sim. Antes que me pergunte, viajo sozinha sim: sem assessores ou acompanhantes. Sou uma atriz diferenciada, não preciso de pessoas atrás de mim! Agora que sabe meus planos, te devolvo a pergunta: para onde vai?\" ")
            print("1 Busco fortunas em terras distantes.")
            print("2 Vou me vingar daqueles que me fizeram sofrer.")
            print("3 Estou seguindo meu coração em busca da pessoa que amo.")
            print("4 Não conte para ninguém, mas sou um fugitivo!")

            verifica_input_int(1, 4, "O que você responde? ")
            
            if entrada == 1:
                print("O sorriso volta a sua face:\"Uau, um aventureiro! Espero que sua aventura seja digna de um filme!", end = '')
            elif entrada == 2:
                print("Ela se espanta e diz: \"Espero que sua vingaça seja digna de um filme!", end = '')
            elif entrada == 3:
                print("Ela se emociona e diz: \"Que lindo! Eespero que seu romance seja digno de um filme!", end = '')
            else:
                print("Ela se exalta e diz: \"que excitante! Isso daria um ótimo filme!", end = '')
            
            print("Gostaria muito de escutar sua história, mas estou exausta. Teremos uma longa viagem pela frente e em algum momento gostaria de escuta-la. Agora, se me der licença\". Ela se vira e sai do \"hall\".")
            
        print("Você percebe que ela fica um pouco sem chão, talvez até mesmo ofendida. Ela leva um tempo para se recompor e diz, com ar de superioridade: \"Pelo jeito não é um admirador da sétima arte. Sou Rita von Trotta, atriz. Já atuei em filmes grandiosos como Amor e paixão, Sabotagem das Ilhas, e Estilo de matar!\" ")
        print("1 Hm, bom para você. Adeus.")
        print("2 Se me permite perguntar, o que faz aqui?")
        verifica_input_int(1, 10, "O que você responde? ")
        
        if entrada == 1:
            d001_Mulher()
        else:
            d002_Mulher()
            
            
    def c003_Mulher():
        '''
        3 Claro que sim!
        '''
        print("Seu estranho sorriso aumenta ainda mais. De pronto, ela tira de sua pequena bolsa um pedaço de papel e uma caneta e escreve \"De Rita von Trotta para meu fã, com muito carinho\".", end = '')
        x = input(txt_continua)
        print("Após ela te entregar o papel, ela continua te olhando com aquele sorriso estranhamente grande. Um clima estranho surge entre vocês e você apenas educadamente se afasta.")
 
    def c004_Mulher():
        print("Ela congela. Seus olhom passam a mirar o chão e seu sorriso enormemente grande se desfaz.", end = "")
        x = input(txt_continua)
        print("De repente seus olhos começam a lacrimejar e percebe-se um grande esforço de sua parte para não desatinar em lágrimas.", end = '')
        x = input(txt_continua)
        print("\"É verdade! Sou uma atriz tão péssima que não consigo nem atuar a vida que gostaria de ter! Sou um completo fracasso!.\"", end = '')
        x = input(txt_continua)
        print("Ela sai depressa do saguão, limpanpo as lágrimas que não conseguiu segurar. Durante um tempo, todos te olham, até que, passado um tempo, perdem o interesse pelo ocorrido e voltam a seus afazeres.")

        
    print("\nVocê se aproxima da bela mulher e antes que possa dizer algo, ela vira para você e com um enorme e estranho sorriso no rosto diz: \"quer um autógrafo, querido?\", e você responde:\n")
    print("1 Um autógrafo seu? Nem pensar!")
    print("2 Me desculpe mas, quem é você?")
    print("3 Claro que sim!")
    print("4 Não acho que uma pessoa realmente famosa estaria num barquinho mequetrefe como esses.")
    verifica_input_int(1, 4, "O que você responde? ")
    
    if entrada == 1:
        c001_Mulher()
    elif entrada == 2:
        c002_Mulher()
    elif entrada == 3:
        c003_Mulher()
    elif entrada == 4:
        c004_Mulher()
    
    Remover_tripulante('mulher')
    Volta_saguao() 
   
def b002_Gala():
    print("Galã")
    
def b003_Capitao():
    print("Capitão")

def b004_Soldado():
    print("Soldado")

def b005_Pai():
    print("Pai")

def b006_Poker():
    print("Poker")

def b007_Mafioso():
    print("Mafioso")

def b008_Capanga():
    print("Capanga")

def b009_Prefeito():
    print("Prefeito")

def b010_Quieto():
    print("Quieto")

    
Intro_001()