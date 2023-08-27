class Review:
    
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
    
    @property
    def rating(self):
        return self._rating
    
    def all():
        pass
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def restaurant(self):
        return self._restaurant