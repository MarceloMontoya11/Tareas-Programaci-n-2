import math
class Punto:
    def __init__(self, c_1=0, c_2=0,c_3=0,c_4=0):
            self.c_1=c_1
            self.c_2=c_2
            self.c_3=c_3
            self.c_4=c_4

    def __str__(self):
        return f" ({self.c_1},{self.c_2})"
    def cuadrante(self):
        if self.c_1==0 and self.c_2!=0:
            print(f"{self} se situa sobre el eje Y ")
        elif self.c_1!=0 and self.c_2==0:
            print(f"{self} se situa sobre el eje X ")
        elif self.c_1==0 and self.c_2==0:
            print(f"{self} se situa sobre el origen")
        elif self.c_1>0 and self.c_2>0:
            print(f"{self} se sitúa en el primer cuadrante")
        elif self.c_1<0 and self.c_2>0:
            print(f"{self} se sitúa en el segundo cuadrante")
        elif self.c_1<0 and self.c_2<0:
            print(f"{self} se sitúa en el tercer cuadrante")
        elif self.c_1>0 and self.c_2<0:
            print(f"{self} se sitúa en el cuarto cuadrante")
   
    def vector(self):
        
        vx=self.c_3-self.c_1
        vy=self.c_4-self.c_2
        print("El vector formado es:",vx,",",vy)
    
    def distancia(self):
        D=math.sqrt((self.c_3-self.c_1)**2+(self.c_4-self.c_2)**2)
        print("La distancia entre los 2 puntos es:",D)


p=input("Digite los 2 puntos deseados, ejemplo:2,5-3,6:")
n=p[p.find("-")+1:len(p)]
x_1=int(p[0:p.find(",")])
y_1=int(p[p.find(",")+1:p.find("-")])
x_2=int(n[0:n.find(",")])
y_2=int(n[n.find(",")+1:len(n)])



cor=Punto(x_1,y_1,x_2,y_2)
print(cor)
cor.cuadrante()
cor.vector()
cor.distancia()