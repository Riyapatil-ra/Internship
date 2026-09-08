'''Stack with Python'''

'''A stack is a linear data structuree that follows the Last-In-First-Out (LIFO) principle.

The main operations of a stack are:
- Push: Adds an element to the top of the stack.
- Pop: Removes the top element from the stack.
- Peek: Returns the top element of the stack without removing it.
- isEmpty: Checks if the stack is empty.
-Size: Finds the number of elements in the stack.

x=[5,56,3,1,9]
push(10)
x=[5,56,3,1,9,10]
push(20)
x=[5,56,3,1,9,10,20]
pop()
x=[5,56,3,1,9,10]
peek()
return 10
pop()
pop()
pop()
pop()
pop()
pop()
x is empty:
return 'EMPTY'
len(x)
return 0

* overflow: If the stack is full and we try to push an element, 
it will result in a stack overflow.
* underflow: If the stack is empty and we try to pop an element,
it will result in a stack underflow.
'''

class Stack:
    size=int(input("Enter the size of the bag: "))
    stack=[0]*size
    top=-1

    def Overflow(self):
        if (self.top==self.size-1):
            return True
        return False

    def Underflow(self):
        if (self.top==-1):
            return True
        return False    

    def push(self,data):
        if self.Overflow():
            print("\nBag Overflow\n")
        else:
            self.top+=1
            self.stack[self.top]=data

    def Pop(self):
        if self.Underflow():
            print("\nBag Underflow\n")
        else:
            data=self.stack[self.top]
            self.top-=1
            print("\nRemoved from the bag:",data)
            print("\n")

    def Size(self):
        print("\nSize of the bag is:",len(self.stack[:self.top+1]))

    def Peek(self):
        if self.Underflow():
            print("\nBag is empty\n")
        else:
            print("\nTop of the bag is:",self.stack[self.top])

    def display(self):
        if self.top==-1:
            print("\nBag is empty\n")
        else:
            print("\nThings in the bag are:")
            for i in range(self.top,-1,-1):
                print(self.stack[i])
            print("\n")
s=Stack()
choice=1
while choice!=0:
    print("Bags")
    print("1. Add things in the bag")
    print("2. Remove things from the bag")
    print("3. Size of the bag")
    print("4. Peek at the top of the bag")
    print("5. Display things in the bag")
    print("0. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        data=input("Enter the things to put in the bag: ")
        s.push(data)
    elif choice==2:
        s.Pop()
    elif choice==3:
        s.Size()
    elif choice==4:
        s.Peek()
    elif choice==5:
        s.display()
    elif choice==0:
        print("Exit")
        break

''' Common Stack Applications:
* Undo/Redo operations in text editors
* Browser history (back/forward)
* Function call stack in programming
* Expression evaluation
'''
''' Advantages of Stack:
* Simple and easy to implement
* Efficient memory usage
* LIFO (Last In, First Out) principle ensures that the most recently added element is the first one to be removed.
'''
''' Disadvantages of Stack:
* Limited size (fixed size stack can lead to overflow)
* Not suitable for all types of problems (e.g., problems that require random access to elements)
* Can be less efficient than other data structures for certain operations (e.g., searching for an
 element in the stack)
'''

''' Time Complexity of Stack Operations:
* Push: O(1)
* Pop: O(1)
* Peek: O(1)
* Size: O(1)
'''
''' Space Complexity of Stack:
* O(n), where n is the number of elements in the stack. 
The space complexity is linear because we need to store all the elements in the stack.
'''