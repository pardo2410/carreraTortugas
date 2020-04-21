import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-30,-10,10,30)
    __colorT= ('red','blue','pink','yellow')
 
# Ajuste de la pantalla
    def __init__(self,width,height):
#        self.width = width
#        self.height = height
        
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('green')
        self.__starline = -width/2 + 20
        self.__finishline = width/2 + 20
        self.__createRunners()

#caracteristicas de las tortugas
    def __createRunners(self):
        
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorT[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__starline, self.__posStartY[i])
                        
            self.corredores.append(new_turtle)
 
#funcion de carrera de tortugas
    def competir(self):
        ganador = False
        
        while not ganador:
            for tortuga in self.corredores:
              avance = random.randint(1,6)
              tortuga.forward(avance)
              if tortuga.position()[0] >= self.__finishline:
                  ganador = True
                  print('La tortuga de color {} ha ganado'.format()[0])
          
             
 
if __name__=='__main__':
    circuito = Circuito(640, 480)
    circuito.competir()
