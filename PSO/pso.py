from Particula import Particula
from City import City
import operator
from Fitness import Fitness
list_city = [City(city.split(",")[0], city.split(",")[-1].replace("\n",""))  for city in open("cidades.txt", "r") ]

class PSO:

    def __init__(self,list_city, pop, c1 , c2, w, iteracoes):
      
        self.population = [ Particula(list_city) for i in range(0,pop)] # montar uma solução
        posBest = self.order_routes(self.population)[0][0]  # pegar a posição da melhor solução
        self.gbest = self.population[posBest] # gbest
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
                # print("Tamanho: {}".format(len(particula.posicao)))
                self.gbest =  particula.move(self.w, self.c1, self.c2, self.gbest)
                
                #print("posicao: {} , gbest: {}, tam: {}".format(particula.fitness,Fitness(self.gbest.posicao).route_fitness(), len(particula.posicao)))
                #print(particula.fitness)
            progress.append(1 / Fitness(self.gbest.posicao).route_distance())
            
        print("Distância Final: " + str(Fitness(self.gbest.posicao).route_distance()) )  




pso = PSO(list_city,200, 0.5, 0.8,0.5, 800)           

pso.runPso()



    

