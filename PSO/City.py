class City:
 #classse que reprenta uma cidade    
    def __init__(self, x,y):
        self.x = int(x) # coordenadas da cidades 
        self.y = int(y)

    def euclidianDistance(self,city):
        #funcão que retorna a distância euclidiana de duas cidades
        return ((self.x - city.x)**2 + (self.y - city.y)**2)**0.5
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def __eq__(self, o):
        return self.x == o.x and self.y == o.y