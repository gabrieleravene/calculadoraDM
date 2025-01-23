# Avaliação de Risco de Diabetes Tipo 2

Este é um programa em Python que realiza uma avaliação personalizada do risco de desenvolver diabetes tipo 2. Ele faz perguntas ao usuário, calcula uma pontuação baseada em fatores de risco e apresenta o resultado final com uma mensagem sobre o nível de risco.

## 🎯 Funcionalidades

- Calcula o Índice de Massa Corporal (IMC) com base no peso e altura.
- Considera fatores como:
  - Idade.
  - IMC.
  - Histórico familiar de diabetes.
  - Pressão arterial alta.
  - Glicemia alta.
- Fornece uma mensagem personalizada com base na pontuação final e o nível de risco.

---

## 🛠️ Como executar o programa

### Pré-requisitos
- Python 3.6 ou superior instalado em seu computador.

### Passo a passo
1. **Clone ou faça o download deste repositório**:
   ```bash
   git clone https://github.com/seu-usuario/risco-diabetes.git

---

## 📊 Como funciona o cálculo de risco?
O programa atribui pontuações com base nas respostas do usuário:

O programa atribui pontuações com base nas respostas do usuário:

**1. Idade:**

45 a 54 anos: +2 pontos
55 a 64 anos: +3 pontos
Mais de 64 anos: +4 pontos

**2. IMC (Índice de Massa Corporal):**

25 a 30: +1 ponto
Acima de 30: +3 pontos
Pressão arterial alta:

**3. Usuários que tomam remédios: +2 pontos**

**4. Glicemia alta:**
Histórico de glicemia alta: +2 pontos

**5. Histórico familiar:**

Pais, irmãos ou filhos com diabetes: +5 pontos
Avós, tios ou primos de primeiro grau com diabetes: +3 pontos
Resultado final
Baixo risco: 0 a 7 pontos
Risco um pouco elevado: 8 a 11 pontos
Risco moderado: 12 a 14 pontos
Risco alto: 15 a 20 pontos
Risco muito alto: Mais de 20 pontos
