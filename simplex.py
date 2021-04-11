class Simplex:

    def __init__(self):
        self.table = [] # tabela para fazer as operações

    def set_objective_funtion(self, objec_func: list):
        """ Função para setar a função objetivo do problema"""

        # A primeira linha da tabela é a função objetivo
        self.table.append(objec_func)

    def add_restrictions(self, restrictions):
        """Função para adiocionar as restrições da função objetivo"""
        self.table.append(restrictions) # Adicionar uma restrição

    def get_entry(self): 
        """ Pegar """
        return self.table[0].index(min(self.table[0])) # pegar o menor valor da que acompanha as variáveis da função objetivo

    def get_exit(self, entry):
        """ Função para pegar o indice da linha que irá sair"""
        # Fazer a divisão do útimo termo da linha b pelo pivor da própria linha
        divs = {} 
        for idx,line in enumerate(self.table): # Pegar as linhas menos a primeira
            if idx > 0 and line[entry] > 0:
               divs[idx] = line[-1]/line[entry]

        return min(divs,key=divs.get) # retornar o menor valor

    def calc_new_pivot(self, entry, exit_c):

        line = self.table[exit_c]
        pivot = line[entry]

        return [value/pivot for value in line]

    def new_line(self, line, entry, pivot_line):
        """ Função que calculará a nova linha""" 
        pivot = line[entry]*-1 # trocar o sinal da linha
       
        result = [value*pivot for value in pivot_line]

        new_line = []
        for i in range(len(result)):
            new_line.append(result[i] + line[i])
        
        return new_line 

    def has_negative_first_line(self):  # condição de parada do algoritmo

        first_line = list(filter(lambda x: x < 0, self.table[0])) # faz uma lista com números negativos
        return len(first_line) > 0
    

    def print_table(self):
        for line in self.table:
            for colum in line:
                print(f"{colum}\t",end="")
            print()
        
    def calculate(self):

        entry  = self.get_entry()
        first_line_exit = self.get_exit(entry)

        pivot_line = self.calc_new_pivot(entry,first_line_exit)

        self.table[first_line_exit] = pivot_line

        table_copy = self.table.copy()

        index = 0
        while index < len(self.table):
            if index != first_line_exit :
                line = table_copy[index]
                new_line = self.new_line(line,entry,pivot_line)
                self.table[index] = new_line
            index+=1 

    def run(self):

        self.calculate()
        while self.has_negative_first_line() :
            self.calculate()

        self.print_table()



simplex = Simplex()
simplex.set_objective_funtion([1,-5,-2,0,0,0])
simplex.add_restrictions([0,2,1,1,0,6])
simplex.add_restrictions([0,10,12,0,1,60])
simplex.run()

