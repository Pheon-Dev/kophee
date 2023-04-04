from django.db import models

class User(models.Model):
    pass
    
class Table(models.Model):
    table_number = models.IntegerField()
    
class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    waiter = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.TextField()
    price = models.IntegerField()
