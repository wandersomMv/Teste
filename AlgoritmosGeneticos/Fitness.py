import City
class Fitness:

    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0

    def route_distance(self):
        """ Função que retorna a distancia de uma rota"""
     
        if self.distance != 0:
            return self.distance
        
        way_distance = 0

        for i  in range(0,len(self.route)): # passar por todas as cidades
            from_city = self.route[i]
            to_city = None

            # verificar se é a cidade onde começou
            to_city = self.route[i+1] if(i+1 < len(self.route)) else self.route[0]

            way_distance += from_city.euclidianDistance(to_city)
        
        self.distance = way_distance

        return self.distance
    
    def route_fitness(self):

        return 1/float(self.route_distance()) if self.fitness == 0 else self.fitness

    