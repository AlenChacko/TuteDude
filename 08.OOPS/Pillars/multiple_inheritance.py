# child inherits multiple parents


class Phone:
    def call(self):
        print("Calling feature")


class Camera:
    def take_photo(self):
        print("Taking photo")


class SmartPhone(Phone, Camera):
    def browse(self):
        print("Browsing web")


sp = SmartPhone()
sp.call()
sp.take_photo()
sp.browse()


# Python follows MRO to resolve conflicts.
# Method Resolution Order (MRO)
print(SmartPhone.__mro__)
