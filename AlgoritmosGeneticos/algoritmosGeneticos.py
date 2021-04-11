import random
import numpy as np
import pandas as pd
from Fitness import Fitness
from City import City
import matplotlib.pyplot as plt
import operator


class AGviajante:

    
    def new_route(self,city_list):
        #funão para fazer uma rota aleatória 
        rota = random.sample(city_list, len(city_list))
        return rota

    def init_population(self, pop_size,city_list):
        """ Retorna uma população (cidades) """
        population = []
        for i in range(0,pop_size):
            population.append(self.new_route(city_list))
        return population
    
    #A função de selção reecebe como parametro a saida da função order_routes
    #para determinar qual rota utilizar
    def seletion(self, popRank, eliteSize):
        
        selection_results = []
        df = pd.DataFrame(np.array(popRank),columns=["Index","Fitness"])
        
        df['cum_sum'] = df.Fitness.cumsum()
        df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
        # Adição do elitismo
        for i in range(0,eliteSize):
            selection_results.append(popRank[i][0])
        
        #aqui é feita a comparação de um número aleatŕio com esses pesos relativos
        #de aptidação para selecionar os indivíduos para etapa de "procriação"

        for i in range(0, len(popRank)-eliteSize):
            pick = 100*random.random()
            for i in range(0,len(popRank)):
                if pick <= df.iat[i,3]:
                    selection_results.append(popRank[i][0])
                    break

        return selection_results

    
    def order_routes(self,population):

        fitness_results = {}
        for i in range(0,len(population)): # calculo das distancias de todas as rotas 
            fitness_results[i] = Fitness(population[i]).route_fitness()

        return sorted(fitness_results.items(),key = operator.itemgetter(1),reverse = True) # ordenando as rotas de acordo com as distancias
    
    #Pegar o resultado da seleção anterior e busca esses indivíduos da nossa população
    def mating_pool(self, population,selection_results):
        matingpool = []
        for i in range(0, len(selection_results)):
            index = selection_results[i]
            matingpool.append(population[index])
        return matingpool
    
    def cross_over(self, parent1, parent2):
        child = []
        childP1 = []
        childP2 = []

        geneA = int(random.random()*len(parent1))
        geneB = int(random.random()*len(parent2))

        startGene = min(geneA, geneB)
        endGene = max(geneA,geneB)

        for i in range(startGene,endGene):
            childP1.append(parent1[i])

        childP2 = [item for item in parent2 if item not in childP1]

        child = childP1 + childP2
        
        return child
    
    def breedPopulation(self,matingpool,eliteSize):
        children = []
        length = len(matingpool) - eliteSize
        pool = random.sample(matingpool, len(matingpool))

        for i in range(0, eliteSize):
            children.append(matingpool[i])

        for i in range(0, length):
            child = self.cross_over(pool[i], pool[len(matingpool)-i-1])
            children.append(child)
        
        return children
    
    def mutate(self, individual, mutation_rate):

        for swapped in range(len(individual)):
            if(random.random() < mutation_rate):
                swapWith = int(random.random()*len(individual))

                city1 = individual[swapped]
                city2 = individual[swapWith]

                individual[swapped] = city2
                individual[swapWith] = city1

        return individual
    
    def mutate_population(self, population, mutation_rate):

        mutatedPop = []
        for ind in range(0, len(population)):
            mutatedInd = self.mutate(population[ind], mutation_rate)
            mutatedPop.append(mutatedInd)
        return mutatedPop
    
    def prox_generation(self, current_gen, eliteSize,mutation_rate):

        popRanked = self.order_routes(current_gen)
        selection_results = self.seletion(popRanked, eliteSize)
        matingpool = self.mating_pool(current_gen, selection_results)
        children = self.breedPopulation(matingpool, eliteSize)
        next_gen = self.mutate_population(children, mutation_rate)
        return next_gen


    def geneticAlgorithmPlot(self,population, popSize, eliteSize, mutationRate, generations):

        pop = self.init_population(popSize, population)  
        
        print("Distância Inicial: " + str(1 / self.order_routes(pop)[0][1]))
        progress = []
        progress.append(1 / self.order_routes(pop)[0][1])
        
        for i in range(0, generations):
            
            pop = self.prox_generation(pop, eliteSize, mutationRate)
            progress.append(1 / self.order_routes(pop)[0][1])
        
        print("Distância Final: " + str(1 / self.order_routes(pop)[0][1]))
        bestRouteIndex = self.order_routes(pop)[0][0]
        bestRoute = pop[bestRouteIndex]
        print("Melhor rota:", bestRoute)
        x = [] 
        y = []
        for r in bestRoute:
           x.append(r.x)
           y.append(r.y)
        
        plt.figure(1)
        plt.subplot(211)
        plt.plot(x,y,'o')
        plt.plot( x, y, 'k-', color='red') # linha pontilha red

        plt.subplot(212)
        plt.plot(progress)
        plt.ylabel('Distância')
        plt.xlabel('Geração')

        plt.show()

ag = AGviajante()
berlin = [City(city.split(",")[0], city.split(",")[-1].replace("\n",""))  for city in open("cidades.txt", "r")] # ler as cidades
ag.geneticAlgorithmPlot(population = berlin,popSize=200, eliteSize=55, mutationRate=0.001, generations = 800)