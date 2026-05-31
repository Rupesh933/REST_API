from django.db import models

# Create your models here.

class Products(models.Model):
    prd_id = models.CharField(max_length=50)
    prd_name = models.CharField(max_length=100)
    prd_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.prd_name