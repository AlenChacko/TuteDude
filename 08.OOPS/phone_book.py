class PhoneBook:
    phone_directory = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        PhoneBook.phone_directory.append(self)

    def show_contact(self):
        print(f"Name:{self.name}, Contact:{self.phone}")

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts exists")
        else:
            for contact in cls.phone_directory:
                contact.show_contact()

    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name == search_name:
                contact.show_contact()
                return
        print(f"{search_name} not found")

    @staticmethod
    def validate_phone(phone):
        if len(phone) == 10 and phone.isdigit():
            return True
        else:
            return False


c1 = PhoneBook("Alen", 9497226368)
c2 = PhoneBook("Amal", 7543932324)
# c1.show_contact()
PhoneBook.show_all_contact()
PhoneBook.search_contact("Alen")
