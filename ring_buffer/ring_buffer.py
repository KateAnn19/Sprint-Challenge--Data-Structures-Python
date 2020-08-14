class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity 
        self.size = 0
        self.index = 0
        
    def __len__ (self):
        return self.size
        
    def append (self, item):
        if self.size == 0:
            self.data.append(item)
            self.size += 1
            return 
        if len(self.data) == self.capacity:
            print(self.index)
            self.size -= 1
            self.data[self.index] = item
            self.size += 1 
            if (self.index + 1) == (self.capacity): 
                self.index = 0
            else: 
                self.index += 1
            return
        if  len(self.data) < self.capacity:
            print("buffer not full")
            self.data.append(item)
            self.size += 1
            return

    def get(self):
        if self.size == 0:
            print("Ring Buffer is Empty \n")
        else:
            return self.data
           

    def __str__(self):
        output = ''
        for i in range(len(self.data)):
            output += f'{self.data[i]} ->'
        return output.format(self=self)
                