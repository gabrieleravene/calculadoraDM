# programa que realiza uma avaliação de risco do diabetes tipo 2
# a cada dado inserido pelo usuário é atribuído uma pontuação e somado ao risco de desenvolver diabetes
# ao final, é exibido uma mensagem ao usuário informando-o sobre sua pontuação final e o risco de desenvolver a doença

def calculoDiabetes():
    print('Avaliação de risco de diabetes tipo 2.')
    nome = input('Antes de começarmos, nos diga qual é o seu nome: ')
    print(f'Olá {nome}! Vamos começar a avaliação. \n')
    
    try:
        risco = 0
        
        # pergunta ao usuário a sua idade
        idade = int(input('Digite sua idade: '))
        if idade >= 45 and idade <= 54:
            risco += 2
        elif idade > 54 and idade < 64:
            risco += 3
        elif idade > 64:
            risco += 4
            
        # pergunta ao usuário a seu peso, altura e calcula o imc
        peso = float(input('Digite o seu peso: '))
        altura = float(input('Digite sua altura: '))
        imc = peso / (altura**2)
        if imc >= 25 and imc <= 30:
            risco += 1
        elif imc > 30:
            risco += 3
            
        # pergunta ao usuário sobre o uso de medicamentos para pressão alta
        pressaoAlta = input('Você toma remédios para pressão alta? Responda SIM ou NÃO').strip().upper()
        if pressaoAlta == 'SIM':
            risco += 2

        # pergunta ao usuário sobre seu nível glicêmico
        glicemia = input('Já teve glicemia alta? Responda com SIM ou NÃO').strip().upper()
        if glicemia == 'SIM':
            risco += 2

        # pergunta sobre histórico familiar de diabetes
        historicoF = input('Possui histórico familiar de diabetes? Responda SIM ou NÃO').strip().upper()
        if historicoF == 'SIM':
            grauParentesco = int(input('Digite 1 se o grau de parentesco for pais, irmão/irmã, filho OU 2 se for avós, tia, tio ou primeiro de primeiro grau'))
            if grauParentesco == 1:
                risco += 5
            elif grauParentesco == 2:
                risco += 3

        # avaliação final
        if risco <= 7:
            print(f'{nome}, sua pontuação é {risco}. Você possui um baixo risco de desenvolver diabetes tipo 2.')
        elif risco > 7 and risco <= 11:
            print(f'{nome}, sua pontuação é {risco}. Você possui um risco um pouco elevado de desenvolver diabetes tipo 2.')
        elif risco >= 12 and risco <= 14:
            print(f'{nome}, sua pontuação foi {risco}. Você possui um risco moderado de desenvolver diabetes tipo 2.')
        elif risco >= 15 and idade <= 20:
            print(f'{nome}, sua pontuação é {risco}. Você possui um risco alto de desenvolver diabetes tipo 2.')
        elif risco > 20:
            print(f'{nome}, sua pontuação é {risco}. Você possui um risco muito alto de desenvolver diabetes tipo 2.')
            
    except ValueError:
        print("Por favor, insira apenas números para idade, peso e altura.")