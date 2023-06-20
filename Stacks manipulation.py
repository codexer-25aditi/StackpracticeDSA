
#Stack manipulation using List

# class Stacksy:
#     def __init__(self):
#         self.list=[]
#     #isEmpty function
#     def isEmpty(self):
#         if self.list==[]:
#             return True
#         else:
#             return False
#     def __str__(self):
#         values=reversed(self.list)
#         values=[str(x) for x in self.list]
#         return '\n'.join(values)
#     #push function
#     def push(self,value):
#         self.list.append(value)
#         return "The value has been inserted"
#     #pop function
#     def pop(self):
#         if self.isEmpty():
#             return "The stack is empty"
#         else:
#             return self.list.pop()
#     def peek(self):
#         if self.isEmpty():
#             return "The stack is empty"
#         else:
#             return self.list[len(self.list)-1]
#     #deleting the stack
#     def delete(self):
#         self.list=None
# Customs=Stacksy()
# print(Customs.isEmpty())
# Customs.push(1)
# Customs.push(2)
# Customs.push(3)
# Customs.push(4)
# Customs.push(5)
# #print(Customs)
# print(Customs.pop())
# #print(Customs)
# print("------------")
# print(Customs)
# print(Customs.peek())
# print("------------")
# print(Customs.delete())


# Stack manipulation using list with limit
class Stacks():
    def __init__(self,max):
        self.max=max
        self.list=[]
    def __str__(self):
        values=reversed(self.list)
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    def isFull(self):
        if len(self.list)==max:
            return True
        else:
            return False
    def push(self,value):
        if self.isFull():
            return "The list is full "
        else:
            self.list.append(value)
            return self.list

    Custom=Stacks(4)
    print(Custom.isEmpty())
    print(Custom.isFull())
    print(Custom.push(18))
    print(Custom.push(19))
    print(Custom.push(20))
    print(Custom.push(23))
    print(Custom)



