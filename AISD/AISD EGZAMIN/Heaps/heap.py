from random import randint
def is_heap(heap_list):
    for i in range(1, len(heap_list)):
        left_child = 2 * i
        right_child = 2 * i + 1
        if left_child < len(heap_list) and heap_list[left_child] < heap_list[i]:
            return False
        if right_child < len(heap_list) and heap_list[right_child] < heap_list[i]:
            return False
    return True

class Heap:
    def __init__(self, heap):
        self.heap = [0] + heap

    def __str__(self):
        return str(self.heap)

    def move_down(self, i):
        iterator = i
        condition = True

        while condition:
            max_child = iterator
            left_child = 2 * iterator
            right_child = 2 * iterator + 1

            if left_child < len(self.heap) and self.heap[left_child] < self.heap[max_child]:
                max_child = left_child
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[max_child]:
                max_child = right_child

            if max_child != iterator:
                self.change_elements(iterator, max_child)
                iterator = max_child
            else:
                condition = False

    def move_up(self, i):
        iterator = i
        condition = True
        while condition:
            parent = iterator // 2
            if parent > 0 and self.heap[parent] > self.heap[iterator]:
                self.change_elements(iterator, parent)
                iterator = parent
            else:
                condition = False

    def change_elements(self, i, j):
        pom = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = pom

    def change_value(self, index, new_value):
        old_value = self.heap[index]
        self.heap[index] = new_value
        if new_value > old_value:
            self.move_up(index)
        else:
            self.move_down(index)

    def build_heap_slow(self):  # O(n * log(n))
        for i in range(2, len(self.heap)):
            self.move_up(i)

    def build_heap_fast(self):  # O(n)
        for i in range(len(self.heap) // 2, 0, -1):
            self.move_down(i)




def build_heap_fast_tests():
    for i in range(100):
        heap = Heap([randint(1, 100) for _ in range(100)])
        heap.build_heap_fast()
        assert is_heap(heap.heap)
        print(f"Test {i} passed")

    print("build_heap_fast all tests passed")

build_heap_fast_tests()