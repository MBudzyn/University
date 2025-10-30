class Zad2:
    def __init__(self):
        self.number_of_citys = 0
        self.dict_of_citys_with_neighbours = {}

    def load_data(self):
        self.number_of_citys = int(input())
        for _ in range(self.number_of_citys - 1):
            city1,city2 = map(int,input().split())
            if city1 not in self.dict_of_citys_with_neighbours:
                self.dict_of_citys_with_neighbours[city1] = [city2]
            else:
                self.dict_of_citys_with_neighbours[city1].append(city2)

            if city2 not in self.dict_of_citys_with_neighbours:
                self.dict_of_citys_with_neighbours[city2] = [city1]
            else:
                self.dict_of_citys_with_neighbours[city2].append(city1)
    def road_length(self,start_city,visited,actual_length):
        visited.append(start_city)



    def print_result(self):
        print(self.dict_of_citys_with_neighbours)

    def run(self):
        self.load_data()
        self.print_result()


zad2 = Zad2()
zad2.run()

