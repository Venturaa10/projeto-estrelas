# JOGO DE ADIVINHAÇÃO DAS ESTRELAS DO FUTEBOL
import os

def limpando_terminal():
    '''ESSA FUNÇÃO SERVE PARA LIMPAR O TERMINAL E EVITAR POLUIÇÃO VISUAL NO TERMINAL'''
    os.system('cls')
    
    

def validando_nome():
    '''FUNÇÃO RESPONSAVEL POR VALIDAR O NOME DO USUARIO!
    - EVITAR QUE O USUARIO ENTRE NO JOGO COM O CAMPO NOME VAZIO
    - Metodo Strip -> Retira os espaços vazios do input
    '''
    global usuario
    usuario = input("Digite o seu nome: ")
    
    while len(usuario.strip()) < 4 or len(usuario.strip()) > 16:
        if True:
            limpando_terminal()
            print('NOME INVÁLIDO')
            print('DIGITE UM NOME COM NO MINIMO 3 CARACTERES!\n')
            return validando_nome()

def sair_do_jogo():
    '''FUNÇÃO PARA LIMPAR TERMINAL E MENSAGEM DE LOGOUT DO USUARIO'''
    limpando_terminal()
    print('OBRIGADO POR JOGAR :)\n'.upper())
    
def retorna_ao_menu():
    input('\nDigite uma tecla para continuar: ')
    limpando_terminal()
    texto_opcao()
    jogo()
    # selecionando_jogador()

def mensagem_acertou():
    print('\n ★ 𝐏𝐀𝐑𝐀𝐁É𝐍𝐒, 𝐕𝐎𝐂Ê 𝐀𝐂𝐄𝐑𝐓𝐎𝐔 𝐀 𝐄𝐒𝐓𝐑𝐄𝐋𝐀 ★')

def mensagem_errou():
    print("\n𝐏𝐔𝐓𝐒, 𝐑𝐄𝐒𝐏𝐎𝐒𝐓𝐀 𝐄𝐑𝐑𝐀𝐃𝐀 :( ")

def texto_de_introducao():
    '''ESSA FUNÇÃO SERVE PARA EXIBIR UM TEXTO DE BOAS VINDAS AO USUARIO
    - EXIBE O NOME DO USUARIO
    '''
    introducao1 = f'SEJA BEM-VINDO(A) USUÁRIO(A): {usuario.title()}'
    introducao2 = 'ESSE É UM SIMPLES JOGO DE ADIVINHAÇÃO DAS ESTRELAS DO FUTEBOL'
    linha = '-' * (len(introducao2))
    limpando_terminal()
    print(linha)
    print(f'{introducao1}\n')
    print(f'{introducao2}\n')
    print(linha)
    input('\nDigite uma tecla para acessar as regras do jogo: ')

def regras_do_jogo():
    '''ESSA FUNÇÃO EXIBE AS REGRAS DO JOGO'''
    limpando_terminal()
    print('''
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
         ---> REGRAS PARA AUXILIAR NA BOA JOGATINA <---
          
        OS NOMES DOS JOGADORES SERÃO VALIDOS, CASO:
          
        · SEJA O APELIDO PELO QUAL O MESMO É RECONHECIDO MUNDIALMENTE
        · PRIMEIRO NOME DO JOGADOR
        · A COMBINAÇÃO DE DOIS NOMES NO QUAL O JOGADOR É RECONHECIDO
            EX: Adriano Imperador
          
                        !DIVIRTA-SE!
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨''')
    # input('\nDigite uma tecla continuar: ')
    retorna_ao_menu()

def texto_opcao():
    '''ESSA FUNÇÃO EXIBE AS OPÇÕES DISPONIVEIS PARA O USUARIO ESCOLHER
    - OPÇÕES PARA ACESSAR O QUIZ DE DETERMINADO JOGADOR
    - OPÇÃO PARA LOGOUT
    - OPÇÃO PARA ACESSAR AS REGRAS NOVAMENTE
    '''
    limpando_terminal()
    texto = '---------> JOGO INICIALIZADO <---------'
    print(texto)
    print(f'\nDIVIRTA-SE USUÁRIO(A) {usuario.title()}')
    print('''
=====================================================================
                SELECIONE UMA DAS OPÇÕES ABAIXO:
                        [ 1 ] - JOGADOR 01   
                        [ 2 ] - JOGADOR 02   
                        [ 3 ] - JOGADOR 03   

                DIGITE:
                0 - PARA SAIR DO JOGO
                4 - PARA ACESSAR AS REGRAS 
                                           
=====================================================================
''')    

def texto_dicas():
    '''FUNÇÃO RESPONSAVEL POR EXIBIR O SUBTITULO DE DICAS DO JOGADOR'''
    limpando_terminal()
    texto = '!dicas do jogador!'
    linha = '*' * (len(texto)) #O '*' será de acordo com o tamanho do texto
    print(linha)
    print(f'{texto}'.upper())
    print(linha)

def opcao_invalida():
    '''FUNÇAÕ RESPONSAVEL POR RETORNAR AO MENU CASO O USUARIO DIGITE UMA OPÇÃO INVALIDA'''
    limpando_terminal()
    retorna_ao_menu()

def jogador_neymar(): 
    '''DICAS DO NEYMAR'''
    limpando_terminal()
    texto_dicas()
    print('''
1 - Jogou pelo Santos
2 - Ganhou puskas com um gol feito contra o Flamengo de Ronaldinho
3 - Conquistou a champions league por um dos maiores clubes do mundo
4 - O seu primeiro hat-trick foi contra um time da Escócia
5 - Fez parte de um time historico
'''.upper())

def jogador_messi():
    '''DICAS DO MESSI'''
    limpando_terminal()
    texto_dicas()
    print(''' 
1 - Campeão da Copa do Mundo
2 - Campeão da Copa America
3 - Campeão da Champions League
4 - O seu primeiro hat-trick foi contra o maior campeão da champions league
5 - Nunca ganhou um puskas
'''.upper())

def jogador_cristiano_ronaldo():
    '''DICAS DO CR7'''
    limpando_terminal()
    texto_dicas()
    print('''
1 - Fez gol de bicicleta em final da champions league
2 - Iniciou sua carreira em um time de Portugal
3 - Campeão da Euro League
4 - Tem uma comemoração marcante
5 - Perdeu uma final de champions league contra o Messi
'''.upper())


def jogo():
    '''FUNÇÃO RESPONSAVEL PELA EXECUÇÃO DOS CÓDIGOS APÓS A ESCOLHA DO USUARIO
    - TRATAMENTO DE ERRO COM TRY E EXCEPT CASO O USUARIO DIGITE UMA OPÇÃO INVALIDA
    '''
    try:
        opcao_escolhida = int(input('Selecione um número para selecionar o jogador secreto: ').strip()) 
        
        if opcao_escolhida == 1:
            jogador_neymar()
            resposta1 = input("Digite o nome do jogador: ")
            
            if resposta1.title().strip() == "Neymar" or resposta1.title().strip() == "Neymar Jr" or resposta1.title().strip() =="Neymar Junior":
                mensagem_acertou()
                retorna_ao_menu()                
            else:
                mensagem_errou()
                retorna_ao_menu()


        elif opcao_escolhida == 2:
            jogador_messi()
            resposta2 = input("Digite o nome do jogador: ")

            if resposta2.title().strip() == "Lionel Messi" or resposta2.title().strip() == "Messi":
                mensagem_acertou()
                retorna_ao_menu()

            else:
                mensagem_errou()
                retorna_ao_menu()


        elif opcao_escolhida == 3:
            jogador_cristiano_ronaldo()
            resposta3 = input("Digite o nome do jogador: ")
                    
            if resposta3.title().strip() == "Cristiano Ronaldo" or resposta3.upper().strip() == "CR7":
                mensagem_acertou()
                retorna_ao_menu()

            else:
                mensagem_errou()
                retorna_ao_menu()

        elif opcao_escolhida == 4:
            regras_do_jogo()
        
        elif opcao_escolhida == 0:
            sair_do_jogo()
        
        else:
            print("OPÇÃO INVÁLIDA!")
            retorna_ao_menu()

    except:
        print("OPÇÃO INVÁLIDA!")
        retorna_ao_menu()

def main():
    limpando_terminal()
    validando_nome()
    texto_de_introducao()
    regras_do_jogo()
    texto_opcao()
    jogo()

if __name__ == '__main__':
    main()
