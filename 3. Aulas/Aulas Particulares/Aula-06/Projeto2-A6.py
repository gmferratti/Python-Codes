import turtle

pt = turtle.Turtle()
wn = turtle.getscreen()

#Goto, dou a coordenada e o cursor se mexe
#pt.goto(-50,-50)

#Para frente
#pt.forward(100)

#Para trás
#pt.backward(100)

#Para direita
#pt.right(90)
#pt.forward(100)

#Para esquerda
#pt.left(90)

lista_n = range(4)
for n in lista_n:
  pt.forward(100)
  pt.right(90)

wn.exitonclick()