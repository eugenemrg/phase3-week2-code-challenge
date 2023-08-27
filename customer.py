class Customer:
    
    customers = []
    
    def __init__(self, first_name, last_name):
        self._given_name = first_name
        self._family_name = last_name
        self.customers.append(self)
    
    @property
    def given_name(self):
        return self._given_name
    
    @given_name.setter
    def set_given_name(self, given_name):
        self._given_name = given_name
    
    @property
    def family_name(self):
        return self._family_name
    
    @family_name.setter
    def set_family_name(self, family_name):
        self._family_name = family_name
    
    @classmethod
    def all(cls):
        return cls.customers
    
    