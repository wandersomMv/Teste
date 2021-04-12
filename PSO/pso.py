from Particula import Particula
from City import City
import operator
from Fitness import Fitness
from copy import deepcopy
import matplotlib.pyplot as plt

list_city = [City(city.split(",")[0], city.split(",")[-1].replace("\n",""))  for city in open("cidades.txt", "r") ]

class PSO:

    def __init__(self,list_city, pop, c1 , c2, w, iteracoes):
      
        self.population = [ Particula(list_city) for i in range(0,pop)] # montar uma solução
        posBest = self.order_routes(self.population)[0][0]  # pegar a posição da melhor solução
        self.gbest = deepcopy(self.population[posBest]) # gbest
        self.c1 = c1
        self.c2 = c2
        self.iteracoes = iteracoes
        self.w = w
       
    def order_routes(self,population):

        fitness_results = {}
        for i in range(0,len(population)): # calculo das distancias de todas as rotas
            fitness_results[i] = Fitness(population[i].posicao).route_fitness()

        return sorted(fitness_results.items(),key = operator.itemgetter(1),reverse = True) # ordenando as rotas de acordo com as distancias
    
    def runPso(self):
       
        print("Distância Inicial: " + str(1 / self.order_routes(self.population)[0][1]))
        progress = []
        progress.append(1 / self.order_routes(self.population)[0][1])
        for i in range(0,self.iteracoes):
            print("Iteração : {} \n".format(i))
            for particula in self.population:
               
                self.gbest =  deepcopy(particula.move(self.w, self.c1, self.c2, self.gbest))
                # print("posicao: {} , gbest: {}, tam: {}".format(particula.fitness,1/Fitness(self.gbest.posicao).route_fitness(), len(particula.posicao)))
               
            
            progress.append(1 / Fitness(self.gbest.posicao).route_fitness())
            
        print("Distância Final: " + str(1/Fitness(self.gbest.posicao).route_fitness()) )  
        # print(progress)
        print("Melhor rota:",self.gbest.posicao)
        bestRoute = self.gbest.posicao

        x = [] 
        y = []
        for r in bestRoute:
           x.append(r.x)
           y.append(r.y)
        x.append(bestRoute[0].x)
        y.append(bestRoute[0].y)

        plt.figure(1)
        plt.subplot(211)
        plt.plot(x,y,'o')
        plt.plot( x, y, 'k-', color='red') # linha pontilha red

        plt.subplot(212)
        plt.plot(progress)
        plt.ylabel('Distância')
        plt.xlabel('Geração')

        plt.show()


pso = PSO(list_city,200, 0.5, 0.8,0.5, 100)           

pso.runPso()



    

