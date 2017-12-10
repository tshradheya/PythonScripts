class House:
    rooms = 5

    def numOfRooms(self):
        print("wtf")
        return self.rooms


newOne  = House()

x = newOne.numOfRooms()
print(newOne.rooms + x)
