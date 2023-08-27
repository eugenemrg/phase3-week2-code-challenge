class Review:
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating
    
    def rating(self):
        return self._rating
    
    def all():
        pass