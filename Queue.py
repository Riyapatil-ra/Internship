'''Queue with Python

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.

The main operations of a queue are:
- Enqueue: Adds an element to the rear of the queue.
- Dequeue: Removes the front element from the queue.
- Front: Returns the front element of the queue without removing it.
- Rear: Returns the rear element of the queue without removing it.
- isEmpty: Checks if the queue is empty.
- Size: Finds the number of elements in the queue.
'''
class Queue:
    size=int(input("Enter the size of queue: "))
    queue=[0]*size
    front=-1
    rear=-1
    empty=True
    def Enque(self,data):
        if self.rear==self.size-1:
            print("\nQueue is full!\n")
            self.empty=False
        else:
            if self.front==-1 and self.rear==-1:
                self.front=0
                self.rear=0
                self.queue[self.rear]=data
                self.empty=False
            else:
                self.rear += 1
                self.queue[self.rear]=data
                self.empty=False

    def Deque(self):
        if (self.front==-1 and self.rear==-1) or (self.front==self.size):
            print("\nQueue is empty!\n")
        else:
            data=self.queue[self.front]
            self.front+=1
            print(f"\nDequeued element is: {data}\n")
    
    def display(self):
        if self.front==-1 and self.rear==-1:
            print("\nQueue is empty!\n")
        else:
            print("\nQueue elements are: ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print('\n')


q=Queue()
choice=1
while choice!=0:
    print("Queue Operations")
    print("1. Enque")
    print("2. Deque")
    print("9. Display")
    print("0. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        data=int(input("Enter the data to add: "))
        q.Enque(data)
    elif choice==2:
        q.Deque()
    elif choice==9:
        q.display()
    elif choice==0:
        print("Exit")
        break

