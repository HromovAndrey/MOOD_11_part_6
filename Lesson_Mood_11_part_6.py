# class GrandParent:
#     def run(self):
#         print("I go ")
#
#     def method(self):
#         print("Parent method")
# class Parent(GrandParent):
#     def walk(self):
#         print("I walk")
#
#     def go(self):
#         print("Parent go")
# class Child(Parent):
#     def method(self):
#         print("Child method")
#
# child = Child()
# # child.go()
# # child.walk()
# # child.method()
# #
# # #Множинне успадкування
# # class ClassA:
# #     def  methodA(self):
# #         print("hello from A")
# #
# #     def method(self):
# #         print("method from A")
# # class ClassB:
# #     def methodB(self):
# #         print("Hello from B")
# #
# #     def method(self):
# #         print("method from  B")
# #
# #
# # class ClassC(ClassA, ClassB):
# #     def method(self):
# #         print("modified methodA")
#       def get super(self):
#           print(super)
#
# # obj = ClassC()
# # obj.methodA()
# # obj.methodB()
# # obj.method()
#
# #Змішане успадкування
#
# # class ClassA:
# #     pass
# # class ClassB(ClassA):
# #     pass
# # class ClassC(ClassA):
# #     pass
# # class ClassD(ClassB, ClassC)
# #     pass
# # print(Child.__mro__)
# # print(Child.mro())
# # child = Child()
# # child.method()
#
# # import time
# # print(type(time).__mro__)
# #
# # def func():
# #     return
# # print(type(func))
# #
# # #def check type(var, data_type=int)
# # func.attr = 3
# # print(func.attr)
#
# #print(ClassC.mro())
# print


# class ClassA:
#     def __init__(self, a):
#         self.a = a
#
#
# class ClassB:
#     def __init__(self, b):
#         self.b = b
#
#
# class ClassC(ClassA, ClassB):
#     def __init__(self, a, b, c):
#         super().__init__(a)
#         ClassB.__init__(self, b)
#         self.c = c
#     def get_info(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
#
# obj = ClassC(1,2,3)
# obj.get_info()

class UIElement:
    def __init__(self, functionlity):
        self.functionlity = functionlity
    def display(self):
        print("display UIElement")

class Buttom(UIElement):
    def __init__(self, functionlity, label):
        super().__init__(functionlity)
        self.label = label
    def display(self):
        print("display Buttom ")

class Menu(UIElement):
    def __init__(self, functionlity, text):
        super().__init__(functionlity)
        self.info = text

    def display(self):
        print("display Menu")

class FieldInput(UIElement):
     def display(self):
         print("display Field")

class InteractiveElement:
    def



buttom = Buttom("", "open")
menu = Menu("", "very useful program")
field = FieldInput("", "your login")
buttom.display()
menu.display()
field.display()