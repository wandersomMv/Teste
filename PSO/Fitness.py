import City
class Fitness:

    def __init__(self, route):
        self.route = route

    def route_distance(self):
        """ Função que retorna a distancia de uma rota"""
        #passar por todas as cidades e calcular o tamanho 
        return  sum( self.route[i - 1].euclidianDistance(self.route[i]) for i in range(0,len(self.route)) )
        
    def route_fitness(self):
        return 1/float(self.route_distance()) 

    