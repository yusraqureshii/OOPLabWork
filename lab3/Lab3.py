#EXAMPLE 1
class Time:
    def __init__(self,hour,min):
       self.setHour(hour)
       self.setMin(min)

    def setHour(self,hour):
        if 0<=hour<=23:
            self._hour=hour
        else:
            raise ValueError("invalid hour value")

    def setMin(self,min):
        if 0<=min <=59:
            self._min=min
        else:
            raise ValueError("invalid min value")

    #EXAMPLE2

    def getHour(self):
        return self._hour
    
    def getMin(self):
        return self._min

    t=Time(15,45)
    print(t.getHour())
    t.setHour(22)
    print(t.getHour())

#EXAMPLE3
 
class Person:
    def __init__(self):
        self.age=-1
    def setage(self,age):
        if 0<=age<=100:
            self._age=age
        else:
            raise ValueError("invalid age value")
    def getage(self):
        return self._age
    def display(self):
        print("your age is",self._age)
    p1= Person()
    #print(p1.age) #GivesError.usegetter
    print(p1.getage())
    p1.age=34 #Does not set private attribute.use setter
    p1.setage(34)
    p1.display

#EXAMPLE4

class Student:
    def __init__(self,n,a):
        #self._name=n
        #self._age=age
    #use of setters in constructors
        self.setName(n)
        self.setAge(a)
    def setName(self,n):
        self._name=n
    def setAge(self,a):
        if a<100 and a>0
               self._age=a
        else:
            raise ValueError("age is not proper!")
    def getName(self):
        return self._name
    def getAge(self):
        return self._age
    def display(self):
        print("Name:",self._name,"age:",self._age)

#EXAMPLE5

s1=Student("Ali",22)
s2=Student("Ahmad",23)
a=s1._age#gives error--use getter
s1._age=34 #cannot set this way_use setters
s1.display() #age for s1 is notmodified,it is still 22
s1.setAge(34)
s1.display()
s2.display()

#EXAMPLE6

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __private_method(self):
        print('this is a private method.')

person=Person('John Doe',30)
person._private_method()           #AttributeError:

#ANOTHER WAY

def __init__(self,l,w):
    self._length=l
    self._width=w
@property
def length(self):
    return self._length
@length.setter
def length(self,l):
    self._length=l
def area(self):
    return self._length*self._width

r1=Room(2,3)
print("Area of room is:",r1.area())
r1.length=4
print("Area of room is:",r1.area())
print("Length of room is:".r1.length)

#task

class Room:
    def __init__(self, length, width):
        # private attributes
        self.__length = 0
        self.__width = 0
        # use the setters so validation also works in the constructor
        self.length = length
        self.width = width

    # private helper methods
    def __is_valid(self, value):
        return isinstance(value, (int, float)) and value > 0

    def __calculate_area(self):
        return self.__length * self.__width

    def __calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    # accessor (getter) and mutator (setter) for length
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if self.__is_valid(value):
            self.__length = value
        else:
            print("Invalid length value")

    # accessor (getter) and mutator (setter) for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if self.__is_valid(value):
            self.__width = value
        else:
            print("Invalid width value")

    # public methods that use the private ones
    def area(self):
        return self.__calculate_area()

    def perimeter(self):
        return self.__calculate_perimeter()


r1 = Room(2, 3)
print("Area of room is:", r1.area())
print("Perimeter of room is:", r1.perimeter())

r1.length = 4
print("Length of room is:", r1.length)
print("Area of room is:", r1.area())

r1.width = -5          # invalid value, rejected by the setter
print("Width of room is:", r1.width)

# r1.__calculate_area()   # AttributeError: private method



























