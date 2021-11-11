class mobile:
    def __init__(self, ram, battery):
        self._battery = battery
        self._ram = ram
    def f(self):
        self.y = 0
        return self.battery * self.ram

    def __del__(self):
        print(self._battery)

    def getBattery(self):
        return self._battery

    def setBattery(self, battery):
        self._battery = battery


s = mobile(4, 5000)
#s.battery = 5000
#s.ram = 4
#print(s._battery, s._ram)
#print(s.battery, s.ram)
#print(s.f())
#print(s.y)
#del s
#print(s)

print(s.getBattery())
print(s.setBattery(3000))
print(s.getBattery())
#print('done')