import random
import math    # cos() for Rastrigin
import copy    # array-copying convenience
import sys     # max float
from City import City
from Fitness import Fitness
from copy import deepcopy
class Particula:

  def __init__(self, city_list):
  
    self.posicao  = random.sample(city_list, len(city_list)) # rota aleatório 
    self.fitness = Fitness(self.posicao).route_fitness()
    self.pbest = deepcopy(self)


  def calculoPbest(self,cpy,gbest):
     
   
     ft = Fitness(deepcopy(cpy)).route_fitness()
    #  self.fitness = ft
     if  ft > self.pbest.fitness: # achou um melhor 
        self.pbest.posicao = deepcopy(cpy)
        self.fitness = deepcopy(ft)

     if(ft > gbest.fitness):
       gbest.posicao = deepcopy(cpy)
       gbest.fitness = deepcopy(ft)

     return gbest

    #  print("ft: {} gbest: {}".format(ft,gbest.fitness))
  
  def get_intervalo(self,size,posicao): 
    k = random.randrange(len(posicao))
    newv = []
    for pos in range(0,size):
        newv.append(posicao[k])
        k = k+1 if(k < len(posicao)-1) else 0
    return newv
  
  def join(self,interval,posicao):
    
     new_s = list(filter(lambda x : x  not in interval, posicao )) # filtra o tour
    #  input("Len new {}, interval {}".format(len(new_s), len(interval)))
     rand  = random.randrange(int(len(new_s)))              # posicao aleatoria
     cpy   = new_s[0:rand] + interval + new_s[rand:]          # junta
     return cpy

  def move(self, w, c1, c2, gbest):

    psize = random.randrange(int(c1 * len(self.posicao)) ) # pegar um numero aleatorio para o pbest 
    gsize = random.randrange(int(c2 * len(self.posicao)) ) # pegar um número aleatório gbest
    
    # pegar um intervalo de um vetor
    part1 =  self.get_intervalo(psize,deepcopy(self.pbest.posicao))
    part2 =  self.get_intervalo(gsize,deepcopy(gbest.posicao))
    part1 = list(filter(lambda x : x  not in part2, part1)) # retirar posições repetidas
   
    
    cpy1 = self.join(part1,deepcopy(self.posicao))
    gbest = self.calculoPbest(cpy1, gbest)
    self.posicao = cpy1
    cpy2 = self.join(part2,cpy1) 
    gbest = self.calculoPbest(cpy2, gbest)
    self.posicao = deepcopy(cpy2)
    for i in range( int(w*len(self.posicao)) ):
      k  = random.randrange(len(self.posicao))
      k2 = random.randrange(len(self.posicao))
      self.posicao[k], self.posicao[k2] =  self.posicao[k2], self.posicao[k]
      gbest = deepcopy(self.calculoPbest(self.posicao, gbest))

    return gbest 
      # p = self.posicao[]
  
  
    
