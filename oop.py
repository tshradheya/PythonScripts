import collections

class House:
    rooms = 5

    def numOfRooms(self):
        print("wtf")
        return self.rooms


newOne  = House()

x = newOne.numOfRooms()
print(newOne.rooms + x)

people = {}
people['a'] = 'A';
people['z'] = 'Z';
people['m'] = 'M';
#people = OrderedDict()

#for k,v in people.items():
    #print (v)

print ('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'Z'
d['d'] = 'D'
d['e'] = 'E'
d = collections.OrderedDict()

d1 = d;
for k, v in d1.items():
    print (k, v)

def fname():
    print( '\n'.join([ ('['+ str(idx+1) +'.] ' + first_name) for idx, first_name in enumerate(d1.values()) ]) )

fname()

#print(fname)
