from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    SEX_TYPES=(("Homme","Homme"),
             ("Femme","Femme"),)
    
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    sex=models.CharField(choices=SEX_TYPES,max_length=5)
    age=models.CharField(max_length=12)
    created=models.DateTimeField(auto_now_add=True)
    saved_by=models.ForeignKey(User,on_delete=models.PROTECT)
    
    class Meta:
        verbose_name="Customer"
        verbose_name_plural="Customers"
    
    
    def __str__(self):
        return self.name
    
    


class Invoice(models.Model):
    INVOICE_TYPE=(
        ("R","RECU"),
        ("P","PROFORMA FACTURE"),
        ("F",'FACTURE'),
    )
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    saved_by=models.ForeignKey(User,on_delete=models.PROTECT)
    invoce_date=models.DateTimeField(auto_now_add=True)
    total=models.DecimalField(max_digits=10000,decimal_places=2)
    last_updated=models.DateTimeField(null=True,blank=True)
    is_paid=models.BooleanField(default=False)
    invoce_type=models.CharField(choices=INVOICE_TYPE,max_length=1)
    comment=models.TextField(null=True,max_length=1000,blank=True)
    
    class Meta:
        verbose_name="Invoice"
        verbose_name_plural="Invoices"
        
    def __str__(self):
        return f"{self.customer.name}_{self.invoce_date}"
    
    @property
    def get_total_invoice(self):
        articles=self.article_set.all()
        total=sum([article.get_total_article() for article in articles])
        return total
    
class Article(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    quantity=models.IntegerField(default=1)
    unit_price=models.DecimalField(max_digits=1000,decimal_places=2)
    total=models.DecimalField(max_digits=1000,decimal_places=2)
    
    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
        
    @property
    def get_total_article(self):
        return self.quantity * self.unit_price
