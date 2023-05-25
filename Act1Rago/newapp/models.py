from django.db import models

# Create your models here.
class item(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    objects = models.Manager()
    stock_quantity = models.IntegerField(default=0)

    def getPrice(self):
        return self.item_price

    def getName(self):
        return self.item_name
    
    def getStockQuantity(self):
        return self.stock_quantity

    def __str__(self):
        return ""

class order(models.Model):
    objects = models.Manager()
    total_amount_paid = models.CharField(max_length=255)
    order_date = models.DateField(auto_now_add=True)
    payment_type = models.CharField(max_length=255)

    def __str__(self):
        return ""
    
    def getTotalAmountPaid(self):
        return self.total_amount_paid
    
    def getOrderDate(self):
        return self.order_date

    def getPaymentType(self):
        return self.payment_type
    
class item_order(models.Model):
    objects = models.Manager()
    order = models.ForeignKey('order', on_delete=models.CASCADE)
    item = models.ForeignKey('item', on_delete=models.CASCADE)
    line_total =  models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def getOrderID(self):
        return self.order.id
    
    def getItemID(self):
        return self.item.id
    
    def getLineTotal(self):
        return self.line_total
    
    def getQuantity(self):
        return self.quantity