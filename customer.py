class Customer:
    
    customers = []
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.customers.append(self)
        
    def given_name(self):
        return self._first_name
    
    def set_given_name(self, given_name):
        self._first_name = given_name
    
    first_name = property(given_name, set_given_name)
    
    def family_name(self):
        return self.last_name
    
    def set_family_name(self, family_name):
        self.last_name = family_name
        
    last_name = property(family_name, set_family_name)
    
    @classmethod
    def all(cls):
        return cls.customers
    
    