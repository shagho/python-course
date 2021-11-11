class abc:
    def __init__(self, data1, data2):
        self._data1=data1
        self._data2=data2
    
    def getData1(self):
        return self._data1

    def setData1(self, data1):
        self._data1=data1

    def getData2(self):
        return self._data2

    def setData2(self, data2):
        self._data2=data2

    def data1_data2(self):
        print("i'm in base class")


class abc1(abc):
    def __init__(self, data1, data2, data3):
        super().__init__(data1, data2)
        self._data3=data3

    def getData3(self):
        return self._data3

    def setData3(self, data3):
        self._data3 = data3

    def data1_data2(self):
        print(self._data3)
        #print(self._data1)
        print("i'm in deriaved class")

abc_object = abc(1, 2)
print(abc_object.getData1(), abc_object.getData2())

abc1_object = abc1(1, 2, 3)
print(abc1_object.getData1(), abc1_object.getData2(), abc1_object.getData3())
abc1_object.data1_data2()
