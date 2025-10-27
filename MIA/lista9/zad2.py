class Zad2:

    def __init__(self):
        self.vertex = 0
        self.edges = 0
        self.table_with_edges = []
        self.result_table = []
    def load_data(self):
        self.vertex,self.edges = map(int,input().split())
        for i in range(self.edges):
            self.table_with_edges.append(list(map(int,input().split())))
        for i in range(self.vertex):
            self.result_table.append(0)
    def fill_result_table(self):
        for edge in self.table_with_edges:
            self.result_table[edge[0] -1] +=1
            self.result_table[edge[1] -1] +=1
    def run(self):
        self.load_data()
        self.fill_result_table()
        self.find_topology()

    def find_topology(self):
        ones = 0
        twos = 0
        vertex_1 = 0
        for data in self.result_table:
            if data == 1:
                ones +=1
            if data == 2:
                twos +=1
            if data == self.vertex - 1:
                vertex_1 +=1
        if twos == self.vertex:
            print("ring topology")
        elif twos == self.vertex - 2 and ones == 2:
            print("bus topology")
        elif vertex_1 == 1 and ones == self.vertex - 1:
            print("star topology")
        else:
            print("unknown topology")




zad2 = Zad2()
zad2.run()