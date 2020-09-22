entrada = 0
txt_continua = "..."


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
                print("Input errado. Tente de novo! ", end = '')
                entrada = int(input(flavor_text))
            entrada_correta = True
        except:
            print("Input errado. Tente de novo! ", end = '')

def Restart():
    verifica_input_int(1,2, "Deseja jogar novamente?\n1 Sim.\n2 Não.\n")
    if entrada == 1:
        a00()
        
def Tutorial():
    print("Para jogar, digite o valor da opção desejada e aperter e tecla ENTER")
    print("Sempre que ver três pontinhos \"...\", aperte a tecla ENTER para continuar a história.", end='')
    x = input(txt_continua)
    print("Agora que já sabe como jogar, deseja começar?\n")
    print("1 Sim!")
    print("2 Não!")
    verifica_input_int(1,2)
    
    if entrada == 1:
        a00()
        Restart()
        
def a00():
    def b01():
        '''
        Apertou
        '''
        
        def c01():
            '''
            Foi
            '''
            def d01():
                '''
                Abriu
                '''
                print("Você coloca no chão a tocha que parcamente iluminava seu redor.", end = '')
                x = input(txt_continua)
                print("Você se inclina em direção ao baú e estica seus braços.", end = '')
                x = input(txt_continua)
                print("Quando suas mãos tocam o baú, você sente algo atrás de você", end = '')
                x = input(txt_continua)
                print("Garras grandes e frias agarram seus ombros.", end = '')
                x = input(txt_continua)
                print("A criatura te agarra fortemente pelos ombros e te vira rapidamente, te colocando face a face com ela. Ela quer que você a veja antes de te matar. E oque você vê é amedrontador. ", end = '')
                x = input(txt_continua)
                print("Uma criatura branca, mais pálida que a neve. A boca enorme esboça um sorriso cheio de dentes pontiagudos; os olhos são completamente negros e profuntos.", end = '')
                x = input(txt_continua)
                print("\"Isso não consta nos pergaminhos\", pensa você antes da criatura abrir sua boca enorme em cima de você.")
                print("Esse é seu fim.\n")
                
            def d02():
                '''
                Não abriu
                '''
                print("Óbvio que você não abriu, está morrendo de medo e só quer sair dessa escuridão, ver o sol novamente e se sentir seguro. Você dá meia volta e corre desesperadamente o caminho de volta, ofegante. No desespero, tropeça em algo; sua tocha voa para longe, se choca contra algo e padece pois já lutava para sobreviver nesse meio tão sem ar. Esse foi o fim da sua única fonte de luz.", end = '')
                x = input(txt_continua)
                print("Você se levanta.")
                print("Breu.")
                print("Breu total. Você não enxerga absolutamente nada. Você soa frio, está ofegante e morrendo de medo. Nesse momento você se arrepende de cada escolha feita na sua vida que o trouxe até aqui.")
                print("\"Ao menos eu devia ter aberto o baú\", pensa você, \"pelo menos saberia como é o tesouro com que tanto sonhei.\"", end = '')
                x = input(txt_continua)
                print("A sensação de estar sendo seguido desaparece. Os grunhidos e ruídos que antes escutava agora não mais escuta. Esse é seu fim: no escuro e no silêncio, completamente sozinho.")
            
            print("Você toma coragem e adentra a escuridão. Acende sua tocha para ilumina-lo, mas a luz é fraca pois o ar é pesado e escasso, dficultando também sua respiração. Durante um tempo, nada de demais, apenas um duro chão de pedra. Após escutar uns barulhos estranho repetidas vezes, você sente que está sendo seguido. Na verdade você tem certeza de que está sendo seguindo. Afinal, você sabe que o tesouro é guardado por algo. Antes de adentrar no caminho escuro uma parte de você tinha uma fagulha de esperança de que a criatura já não mais habitasse as catacumbas. Errado. Ela estava lá e ela havia te notado.", end = '')
            x = input(txt_continua)
            print("Após caminhar por esse trajeto horripilante, escuro, e orquestrado por grunhidos aterrorizantes, você vê aquilo que o trouxe até aqui. Lá está, bem na sua frente: o baú que contêm o tesouro que você passou a vida buscando.", end = '')
            x = input(txt_continua)
            print("Porém - e sempre tem um porém - ele é diferente da descrição dos pergaminhos antigos. Ele tem marcas estranhas e emite um som agudo. Se não fosse pela ausência de luz, você até poderia dizer q ele se mexe.\n")
            print("1 - Passei minha vida buscando esse tesouro. Eu preciso dele. Abro o baú sem hesitar.")
            print("2 - Meu sonho está ficando muito arriscado. Talvez se eu abri-lo a criatura se enfeze e não sou capaz de detê-la nesse estado")
            
            verifica_input_int(1, 2)
        
            if entrada == 1:
                d01()
            else:
                d02()
        def c02():
            '''
            Não foi
            '''
            def d03():
                '''
                Esquerda e comida
                '''
                print("esuqerda comida")
    
            def d04():
                '''
                Direta e luxo
                '''
                def e01():
                    '''
                    Pegou o diamante
                    '''
                    print("Num movimento rápido você pega o brilhante diamante e o guarda no bolso!", end = '')
                    x = input(txt_continua)
                    print("Você para por uns instantes, apreensivo, esperando que algo aconteça.", end ='')
                    x = input(txt_continua)
                    print("Você revira os olhos para um lado, e nada. Despois para o outro, e também nada.", end ='')
                    x = input(txt_continua)
                    print("Alívio. Nada aconteceu. Você expele o ar de seus pulmões e seus ombros relaxam. Bem, agora de volta ao objetivo principal: fugir desse lugar horrível!",end ='')
                    x = input(txt_continua)
                    print("Quando você se vira, você escuta o mesmo gruninho que escutou quando apertou botão, só que dessa vez, ele está perto. Na verdade, na sua frente. Lá está a criatura. Ume enorme figura pálida se proteja a sua frente. Alta, esbelta e com garras enormes, desproporcionais ao resto do corpo. Seus olhos, bem, ela não tem olhos, apenas cavidades vazias que miram você.", end='')
                    x = input(txt_continua)
                    print("Você tem algo que é da criatura e ela o quer de volta. A boca da criatura começa a se abrir lentamente. Com medo, você da um pequeno passo para trás, quando de repende a bocarra se abre rapidamente e te engole inteiro.", end = '')
                    x = input(txt_continua)
                    print("Esse é o seu fim.")
                    
                    
                def e02():
                    '''
                    Não pegou o diamante
                    '''
                    print("Você resiste a tentação e deixa o diamante onde está e volta a caminhar reto pelo corredor. De repente algo muda: os quadros já não mais têm retratos, são apenas molduras vazias. Estranho, mas segue em frente.", end ='')
                    x = input(txt_continua)
                    print("De repente, enquanto anda, você escuta um barulho rompe o silêncio do ambiente. É um barulho seco e pontual, como o de uma martelada num pedaço de madeira. Com medo, você se vira já esperando o pior pois se lembra das histórias horríveis que escutou sobre esse lugar.")
                    x = input(txt_continua)
                    print("Quando você se vira completamente, você vê uma moldura com uma tela em branco em pé, bem na sua frente, como se ela te encarasse. Do seu lado esquerdo, há uma lacuna na sequência de quadros que se repetiu ao longo de todo o corredor.", end='')
                    x = input(txt_continua)
                    print("Esse quadro pulou da parede e agora está de pé, mirando você e você mirando a ele. Você não sente mais medo, mas está intrigado. \"Esse quadro está vivo? Como ele pulou da parede? Como ele está de pé sem nenhuma suporte?\"", end='')
                    x = input(txt_continua)
                    print("De repente braços começam a surgir das laterais da moldura, como um galho cresce numa árvore. Você fica desesperado e espantado. E num movimento rápido, os braços te agarram e o quadro te \"engole\". ", end ='')
                    x = input(txt_continua)
                    print("Agora você é mais um retrato de uma pessoa desesperada e espantada pendurado na parede desse luxuoso corredor, e sua vida agora é observar outros tolos aventureiros serem engolidos pelos quadros vazios.", end='')
                    x = input(txt_continua)
                    print("Esse é o seu fim.")
                    
                print("Conforme você vai andando, percebe que os todos os quadros tem algo em comum: são retratos de pessoas com feições desesperadas e espantadas, como quem acabou de levar um susto. Além disso, a mobilia e o luxo vão ficando mais intensos: mais ouro e mais rubis iluminam sua visão.", end = '')
                x = input(txt_continua)
                print("Essa sala é igualmente assustadora e estranha como todas as outras, mas é também tão luxuosa que você luta consigo mesmo para manter o foco em seu objetivo.", end= '')
                x = input(txt_continua)
                print("De repente toda sua atenção é robada por um enorme diamante, do tamanho de um punho de um homem crescido, largado em cima de uma mesa encostada na parede. Nessa mesma parede, em cima dessa mesa, há um quadro de um pessoa tabém com feição de desespero. Você: ")
                x = input(txt_continua)
                print("1 Pego o diamente. Se eu conseguir sair daqui, saio rico!")
                print("2 Tentador, mas melhor deixar onde está. Esse lugar é macabro e vai saber oque há por trás desse diamante.")
                verifica_input_int(1, 2)
        
                if entrada == 1:
                    e01()
                else:
                    e02()

            
            print("\nAo olhar o caminho que se abriu, ao menos o pouco que a fraca luz te permite enxergar, você entede o motivo pelo qual alguém mandou não apertar o botão. Essa passagem é nefasta e não deve conduzir a lugar nenhum se não a um final trágico.", end = '')
            x = input(txt_continua)
            print("Seguindo o seu caminho, você se depara com uma bifurcação. Do lado esquerdo vem um cheiro de comida tão delicioso que sua barriga ronca no exato momento em que o odor adentra suas narinas. Do lado direito, você ve um corredor repleto de obras de arte, mobilias luxuosas e ornamentos de ouro. Qual caminho seguirá?\n")
            print("1 Essa comida deve estar deliciosa. Vou pela esquerda.")
            print("2 Esse corredor é lindo e extravagante. Vou pela direita.")
            verifica_input_int(1, 2)
            
            if entrada == 1:
                d03()
            else:
                d04()
                
            
    
        print("Você escuta um estrondo. Ao seu lado, uma parede secreta se abre e um caminho se revela. Esse caminho porém, é escuro, amedrontador e você escuta uns grunidos abafados vindo do fundo dessa passagem. Um sensação ruim te diz para fugir e que você não devia ter apertado o botão (e se um mosntro sair dai e te comer?). Mas uma outra voizinha da sua caebça te diz pra seguir em frente pois esse é o caminho para O Tesouro.\n")
        print("1 - Eu quero muito esse tesouro. Vou em frente.")
        print("2 - Dane-se o tesouro. Eu quero mais é viver.")
        
        verifica_input_int(1, 2)
        
        if entrada == 1:
            c01()
        else:
            c02()
    
    def b02():
        '''
        Não apertou
        '''
        def c03():
            def d05():
                print("n aperto e fez algo")
            def d06():
                print("n aperto e nao fez algo")
        def c04():
            def d07():
                print("n aperto e fez algo")
            def d08():
                print("n aperto e nao fez algo")
                
    print("\n--------------")
    print("A sua frente há um botão escrito \"NÃO APERTAR\". O que você faz?\n")
    print("1 - Botões foram feitos para serem apertador. Eu aperto.")
    print("2 - A placa diz para não apertar. Logo, não aperto.")
    
    verifica_input_int(1, 2)
    
    if entrada == 1:
        b01()
    else:
        b02()    
   
Tutorial()
         