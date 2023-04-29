from django.db import models

class Table(models.Model):
    table_id = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return(f"{self.table_id} {self.capacity}")
    
    
class Menu(models.Model):
    item = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return(f"{self.price} {self.item}")
    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    menu_item = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return(f"{self.table} {self.menu_item} {self.quantity}")
    
