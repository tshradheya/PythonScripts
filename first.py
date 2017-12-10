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


name = "John"
age = 23
print("%s is %d years old." % (name, age))


data = ("John", "Doe", 53.44)
format_string = "Hello"

print("Hello %s %s. Your current balance is %.2f" % (data[0], data[1], data[2]))


count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for i in numbers:
    if i%2 == 0:
        print(i);
