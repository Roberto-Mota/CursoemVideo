# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar
# módulos em Python e reutilizar nossos códigos em outros projetos. Vamos aprender também
# como agrupar vários módulos em um pacote, ampliando ainda mais a modularização em grandes
# projetos em Python.
import uteis


num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'{num}! = {fat}')