print("Hello, World!")
z = 1;
if z == 1 and isinstance(z,int):
    print("z=1! Indentation for braces!")

#integer

myString = 'hello'
print(myString);
a, b = 3, 4;


myStringNone = None #wow

print("String: %s" %myStringNone)


#Lists

myList = []
myList.append(1);
myList.append(21);

for p in myList:
    print(p);


lotsofhellos = "hello" * 10 # wow wtf
print(lotsofhellos)

print([1,2,3] * 3)


x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = []
big_list = x_list + y_list;

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
