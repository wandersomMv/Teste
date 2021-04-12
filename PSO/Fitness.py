import City
class Fitness:

    def __init__(self, route):
        self.route = route

    def route_distance(self):
        """ Função que retorna a distancia de uma rota"""
        #passar por todas as cidades e calcular o tamanho 
      
        
        way_distance = 0

        for i  in range(0,len(self.route)): # passar por todas as cidades
            from_city = self.route[i]
            to_city = None

            # verificar se é a cidade onde começou
            to_city = self.route[i+1] if(i+1 < len(self.route)) else self.route[0]

            way_distance += from_city.euclidianDistance(to_city)
        
        return way_distance

        
        
    def route_fitness(self):
        return 1/float(self.route_distance()) 

    