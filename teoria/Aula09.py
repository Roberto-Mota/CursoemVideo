# Fase 09 -> Manipulando cadeias de texto
#
# Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são o Fatiamento
# de String, Análise com len(), count(), find(), transformações
# com replace(), upper(), lower(), capitalize(), title(), strip(),
# junção com join().
#
#       Análise de String
#len(frase) #len vem de lenght# -> mede o tamanho da string
#frase.count('o') -> contar quantas vezes aparece a letra o na frase
#frase.count('o',0,13) -> contar quantas vzs aparece ja fatiado
#frase.find('deo') -> mostra em que momento começou 'deo'
#      rfind, lfind
#       (se receber -1 significa que não existe na string)
#'Thatyara' in frase -> operador que diz se existe "Thatyara" na frase
#
#
#       Transformação de String
#frase.replace('Thatyara,'Meu dengo')
#frase.upper() -> vai tudo pra maiusculo
#frase.lower() -> vai tudo pra minusculo
#frase.capitalize() -> Joga tudo pra minusculo e só a primeira fica em maiusculo
#frase.title() -> Vai cudo depois de espaço em maisuculo
#frase.strip() -> remove os espaços inuteis da string (nego que coloca espaço demais pq é burro)
#frase.rstrip() -> a variação r significa right, limpa o lado direito. o mesmo com lstrip, porem na esquerda
#
#       Divisão
#frase.split() -> corta os espaços e cria uma lista com a frase
#
#       Junção
#'-'.join(frase) -> usa o - como separador pra juntar a lista da frase quebrada pelo split
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
frase = 'A Thatyara é uma belezura'
print(frase)
print(frase[1:10])
ordem ='01234567890123456789'
print(ordem[0:5])
print(ordem[:5])
print(ordem[5:10])
print(ordem[10:20])
print(ordem[10:])
print(ordem[5:10:2])
print(ordem[5::3])
contador = (frase.upper().count('A'))
print("A quantidade de 'A's maiúsculos após usar o upper é {}".format(contador))
frase2 = ('Thatyara está estudando')
frase2 = frase2.replace('Thatyara', 'Meu dengo')
print(frase2)
print('-'*50)
texto = ('''Lorem ipsum dolor sit amet, mei sale nostro suavitate ei.''')
import random
textosplit = texto.split()
textoschuffle = random.shuffle(textosplit)
print(textosplit)