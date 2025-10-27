class Zad3:
    def __init__(self):
        self.number_of_islands = 0
        self.table_of_islands = []
        self.number_of_bridges = 0
        self.table_of_bridges = []
        self.table_of_bridge_range = []

    def load_data(self):
        tab_num_isl_brid = input().split()
        self.number_of_bridges= int(tab_num_isl_brid[1])
        self.number_of_islands = int(tab_num_isl_brid[0])
        for i in range(self.number_of_islands):
            tab = input().split()
            self.table_of_islands.append([int(tab[0]),int(tab[1])])
        self.table_of_bridges = input().split()
        for i in range(self.number_of_bridges):
            self.table_of_bridges[i] = int(self.table_of_bridges[i])
        for i in range(1,self.number_of_islands):
            island1 = self.table_of_islands[i-1]
            island2 = self.table_of_islands[i]
            min_bridge = island2[0]-island1[1]
            max_bridge = island2[1] - island1[0]
            self.table_of_bridge_range.append([min_bridge,max_bridge])


