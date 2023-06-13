import turtle
import random
nomes = ['azul', 'vermelha', 'verde', 'amararela', 'roxa']
cores = ['blue', 'red', 'green', 'yellow', 'purple']
seta = turtle.Turtle()
seta.color('black')
seta.penup()
seta.setpos(-330, 160)
vencedora = ""
tartarugas = dict()

pos_inicio = (-330, 150)
espaco = 50

for nome, cor in zip(nomes, cores):
    tartarugas[nome] = turtle.Turtle()
    tartarugas[nome].shape("turtle")
    tartarugas[nome].color(cor)
    pos_x = pos_inicio[0]
    pos_y = pos_inicio[1] - (espaco * len(tartarugas))
    tartarugas[nome].penup()
    tartarugas[nome].setpos(pos_x, pos_y)
    tartarugas[nome].pendown()

aposta = input("Em qual tartaruga deseja apostar? Digite o nome da cor: ").lower()

while not vencedora:
    for nome in nomes:
        distancia = random.randint(1, 10)
        tartarugas[nome].forward(distancia)
        if tartarugas[nome].pos()[0] > 300:
            vencedora = tartarugas[nome].pencolor()
            indice = cores.index(vencedora)
            vencedora = nomes[indice]
            break

if vencedora == aposta:
    mensagem = "Parabéns! Você acertou!"
else:
    mensagem = "Poxa vida! Você errou!"

fonte = ("Comic Sans", 20, "bold") 
seta.write(mensagem, True, "center", fonte)
screen = turtle.Screen()
screen.exitonclick()
