

class Heap:

    def __init__(self) -> None:
        self.array = []
        self.size = 0

    def insert(self, key):
        self.array.append(key)
        self.size += 1
        if self.size > 1:
            self.bubble()

    def bubble(self):
        x = self.array[-1]
        x_index = self.size-1
        parent_index = (x_index - 1)//2
        while x_index != 0 and x < self.array[parent_index]:
            self.array[parent_index], self.array[x_index] = self.array[x_index], self.array[parent_index]
            x_index = parent_index
            parent_index = (x_index-1)//2

    def trickle(self):
        x = self.array[0]
        x_index = 0
        right_index = 2*x_index + 2
        left_index = 2*x_index + 1
        while (x > self.array[right_index] or x > self.array[left_index]):
            if self.array[right_index] < self.array[left_index]:
                self.array[x_index], self.array[right_index] = self.array[right_index], self.array[x_index]
                x_index = right_index
            else:
                self.array[x_index], self.array[left_index] = self.array[left_index], self.array[x_index]
                x_index = left_index

            if x_index == self.size-1:
                return
            right_index = 2*x_index + 2
            left_index = 2*x_index + 1
            if left_index >= self.size:
                return
            elif right_index >= self.size:
                right_index = left_index

    def delete_min(self):
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        minn = self.array.pop(-1)
        self.size -= 1
        self.trickle()
        return minn


h = Heap()
h.insert(3)
h.insert(9)
h.insert(6)
h.insert(8)
h.insert(2)
print(h.array)
h.delete_min()
print(h.array)
