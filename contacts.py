import mixin
class _AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('1 address', 'city', 'state', '00001'),
            2: Address('2 address', 'city', 'state', '00002'),
            3: Address('3 address', 'city', 'state', '00003'),
            4: Address('4 address', 'city', 'state', '00004'),
            5: Address('5 address', 'city', 'state', '00005')
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address

class Address(mixin.Mixin):
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state}, {self.zipcode}")
        return '\n'.join(lines)

_address_book = _AddressBook()

def get_employee_address(employee_id):
    return _address_book.get_employee_address(employee_id)
