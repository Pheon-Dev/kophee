from django.db import models

class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    
class Table(models.Model):
    table_id = models.CharField(max_length=50)
    capacity = models.IntegerField()
    
    
class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    
class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    waiter = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    menu_item = models.TextField()
    
