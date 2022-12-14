class QueueOverflowException(Exception):
    pass
class EmptyQueueException(Exception):
    pass
class Queue():
    # constructor
    def __init__(self, size, threshold): # initializing the class
        self.size = size
        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
        self.threshold = threshold
        self.num_above_threshold = 0
        self.num_data_points = 0
    def set_threshold(self, threshold):
        self.threshold = threshold
    def enqueue(self, data):
        self.num_data_points +=1
        if self.threshold != None and data > self.threshold:
            self.num_above_threshold += 1
        # condition if queue is full
        if ((self.rear + 1) % self.size == self.front):
            print(" Queue is Full\n")
            raise QueueOverflowException
        # condition for empty queue
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    def dequeue(self):
        if (self.front == -1): # condition for empty queue
            print ("Queue is Empty")
            raise EmptyQueueException
        temp=self.queue[self.front]
        self.queue[self.front] = None
        self.num_data_points -= 1
        if self.threshold != None and temp > self.threshold:
            self.num_above_threshold -= 1
        # condition for only one element
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return temp
    def get_array(self):
        return self.queue
    def peek(self):
        return self.queue[self.front]
    def get_size(self):
        return self.num_data_points
    def get_proportion_above_threshold(self):
        #catch div by 0
        return self.num_above_threshold/self.num_data_points

