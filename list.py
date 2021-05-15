list=["c","c++"]
list.append("java")
list.append("python")
print(list)
list.pop()
print(list)
list.pop()
print(list)
list.pop()
print(list)
if not list:
    print("no books are there")


Q=[]
front=None
rear=None


def isempty(que):
    if que==[]:
        return True
    else:
        return False


def enqueue(que,item):
    que.append(item)
    if len(que)==1:
        front=rear=0
    else: 
        rear=len(que)-1 


def dequeue(que):
    if isempty(que):
        return ('overflow')
    else:
        i=que.pop(0)  

    if len(que)==0:
        front=rear=None
    return i    

def peek(que):
    if isempty(que):
        return ('overflow')
    else:
        front=0
        return que[front]

def display(que):
    if len(que)==0:
        return ('queue is empty')
    elif len(que)==1:
        print(que=[0])
    else:
        front=0
        rear=len(que)-1
        print(que[front])
        for x in range(1,rear):
            print(que[x])
        print(que=[rear])


while True:
    print('--THIS IS QUEUE IMPLEMENTATION--')
    print('1. ENQUEUE')  
    print('2. DEQUEUE') 
    print('3.peek')   
    print('4. display')  
    print('5.exit') 
    ch=int(input("Enter the choice between 1-5: "))
    if (ch==1):
        item=int(input("enter the item: "))
        enqueue(Q,item)
        input("press any key to continue: ")
    if (ch==2):
        item=dequeue(Q)
        if(item=='underflow!'):
            print("the queue is empty")
        else:
            print('%d is dequeued!' %item)
        input("press any key")
    if(ch==4):
        display(que)  
        input("press any key")
