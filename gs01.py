import os
import time

listaDeDadosBarragens = []


def limparTela():   
    os.system('cls')


def pausar():
    input('\nPressione ENTER para voltar ao menu')


def aviso():
    print('''\n=================== AVISO ===================
Não é necessário digitar a unidade de medida!
Insira apenas o valor!
=============================================''')
    

def lerSensores():
    try:                
        limparTela()

        print(len('LEITURA DOS SENSORES')*'=')
        print('LEITURA DOS SENSORES')
        print(len('LEITURA DOS SENSORES')*'=')

        aviso()

        barragem = input('\nDigite o nome da barragem: ')
        umidade = float(input('Digite a umidade do solo (%): '))
        inclinacao = float(input('Digite a inclinação da estrutura (°): '))
        deformacao = float(input('Digite o nível de deformação (ε): '))
        temperatura = float(input('Digite a temperatura da área (°C): '))

        dados = {
            'barragem': barragem,
            'umidade': umidade,
            'inclinacao': inclinacao,
            'deformacao': deformacao,
            'temperatura': temperatura
        }

        listaDeDadosBarragens.append(dados)

        print('Sensores analisados com sucesso!')
        pausar()

    except ValueError:
        limparTela()
        print('Erro ao processar informações!')
        pausar()


def calcularVelocidadeDeformacao(deformacao, tempo):
    return deformacao / tempo


def calcularDeformacao():
    try:
        limparTela()

        print(len('CÁLCULO DE DEFORMAÇÃO') * '=')
        print('CÁLCULO DE DEFORMAÇÃO')
        print(len('CÁLCULO DE DEFORMAÇÃO') * '=')

        aviso()

        calculoDeformacao = float(input('\nDigite a deformação total (ε): '))
        calculoTempo = float(input('Digite o tempo monitorado (s): '))

        if calculoTempo == 0:
            raise ZeroDivisionError

        calculoVelocidade = calcularVelocidadeDeformacao(calculoDeformacao, calculoTempo)

        time.sleep(0.5)
        print('\nCalculando...')
        time.sleep(1)

        print(f'\nVelocidade da deformação: {calculoVelocidade:.2f} ε/s')

        pausar()

    except ValueError:
        limparTela()
        print('Erro ao processar informações!')
        pausar()

    except ZeroDivisionError:
        limparTela()
        print('Erro. O tempo não pode ser zero!')
        pausar()


def preverRiscoDeColapso():
        try:
            limparTela()

            print(len('PREVISÃO DE RISCO')*'=')
            print('PREVISÃO DE RISCO')
            print(len('PREVISÃO DE RISCO')*'=')

            aviso()

            velocidade = float(input('\nDigite a velocidade da deformação (ε/s): '))
            umidade = float(input('Digite a umidade (%): '))

            if velocidade >= 4 and umidade >= 70:
                riscoColapso = 'CRÍTICO'
            elif velocidade >= 3:
                riscoColapso = 'ALTO'
            elif velocidade >= 2:
                riscoColapso = 'MÉDIO'
            else:
                riscoColapso = 'BAIXO'

            print(f'\nNível de risco: {riscoColapso}')

            pausar()

        except ValueError:
            limparTela()
            print('Erro ao processar informação!')
            pausar()


def emitirAlerta():
    limparTela()

    print(len('ALERTA DE EMERGÊNCIA')*'=')
    print('ALERTA DE EMERGÊNCIA')
    print(len('ALERTA DE EMERGÊNCIA')*'=')

    time.sleep(1.5)

    print('\n⚠ ALERTA VERMELHO ⚠')

    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')

    print('Evacuação preventiva ativada.')

    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')

    print('Defesa civil acionada.')

    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')

    print('Sirene de emergência ativada.')

    pausar()


def gerarRelatorio():
    limparTela()

    print(len('RELATÓRIO TÉCNICO') * '=')
    print('RELATÓRIO TÉCNICO')
    print(len('RELATÓRIO TÉCNICO') * '=')

    if len(listaDeDadosBarragens) == 0:
        print('\nNenhuma barragem monitorada ainda.')
        pausar()
        return

    ultimaBarragem = listaDeDadosBarragens[-1]

    deformacaoRelatorio = ultimaBarragem['deformacao']
    umidadeRelatorio = ultimaBarragem['umidade']

    if deformacaoRelatorio >= 4 and umidadeRelatorio >= 70:
        riscoRelatorio = 'CRÍTICO'
        statusRelatorio = 'RISCO DE ROMPIMENTO'
    elif deformacaoRelatorio >= 3:
        riscoRelatorio = 'ALTO'
        statusRelatorio = 'MONITORAMENTO URGENTE'
    elif deformacaoRelatorio >= 2:
        riscoRelatorio = 'MÉDIO'
        statusRelatorio = 'EM OBSERVAÇÃO'
    else:
        riscoRelatorio = 'BAIXO'
        statusRelatorio = 'ESTÁVEL'

    time.sleep(1)
    print('Gerando relatório...')
    time.sleep(1)

    dataHora = time.strftime('%d/%m/%Y - %H:%M:%S')

    print(f'''
Barragem Monitorada: {ultimaBarragem['barragem']}

================ DADOS DOS SENSORES ================
Umidade do solo: {ultimaBarragem['umidade']}%
Inclinação da estrutura: {ultimaBarragem['inclinacao']}°
Deformação: {ultimaBarragem['deformacao']} ε
Temperatura: {ultimaBarragem['temperatura']}°C

================ RESULTADO DA ANÁLISE ================
Nível de risco: {riscoRelatorio}
Status da barragem: {statusRelatorio}

Data e horário da análise:
{dataHora}
=====================================================
''')

    pausar()


def historicoDeBarragens():
    limparTela()

    print(len('HISTÓRICO DE BARRAGENS') * '=')
    print('HISTÓRICO DE BARRAGENS')
    print(len('HISTÓRICO DE BARRAGENS') * '=')

    if len(listaDeDadosBarragens) == 0:
        print('\nNenhum histórico encontrado.')
        pausar()
        return

    contador = 1

    time.sleep(1)
    print('Carregando...')
    time.sleep(1)

    for dados in listaDeDadosBarragens:
        print(f'''
================ REGISTRO {contador} ================
Barragem: {dados['barragem']}
Umidade: {dados['umidade']}%
Inclinação: {dados['inclinacao']}°
Deformação: {dados['deformacao']} ε
Temperatura: {dados['temperatura']}°C
====================================================''')
        
        contador += 1

    pausar()


def sobreProjeto():
    limparTela()

    print(len('SAFE EARTH')*'=')
    print('SAFE EARTH')
    print(len('SAFE EARTH')*'=')
    print('')
    print(len('Sistema de monitoramento de barragens')*'=')
    print('''Sistema de monitoramento de barragens
utilizando sensores e tecnologia espacial.
O projeto busca prevenir tragédias
através da análise de deformações.''')
    print(len('Sistema de monitoramento de barragens')*'=')

    pausar()


def encerrarSistema():
    limparTela()
    time.sleep(0.5)
    print('Encerrando sistema...')
    time.sleep(1)
    limparTela()


def menu():
    while True:
        try:
            limparTela()
            print('''===============================
SAFE EARTH - MONITORAMENTO
===============================
1 - Ler Sensores
2 - Calcular Deformação
3 - Prever Risco de Colapso
4 - Emitir Alerta
5 - Gerar Relatório
6 - Histórico de Barragens
7 - Sobre o Projeto
8 - Encerrar Sistema
===============================''')
            
            opcao = int(input('Escolha uma opçao: '))
            match opcao:
                case 1:
                    lerSensores()
                case 2:
                    calcularDeformacao()
                case 3:
                    preverRiscoDeColapso()
                case 4:
                    emitirAlerta()
                case 5:
                    gerarRelatorio()
                case 6:
                    historicoDeBarragens()
                case 7:
                    sobreProjeto()
                case 8:
                    encerrarSistema()
                    break
                case _:
                    limparTela()
                    print('Opção inválida')
                    pausar()
                
        except ValueError:
            limparTela()
            print('Erro. Digite apenas 1-2-3-4-5-6-7-8')
            pausar()

menu()