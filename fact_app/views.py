from django.shortcuts import render
from django.views import View
from .models import Invoice,Customer
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'base.html')


class HomeView(View):
    templates_name="index.html"
    invoices=Invoice.objects.select_related("customer","saved_by").all()
    
    context={
        'invoices':invoices
    }
    
    def get(self,request, *args, **kwargs):
        return render(request,self.templates_name,self.context)
    
    def post(self,request, *agrs, **kwargs):
        return render(request,self.templates_name,self.context)
        
        
        
class AddCustomerView(View):
    templates_name="add_customer.html"
    context={}
    
    def get(self,request, *args, **kwargs):
        return render(request,self.templates_name)
    
    def post(self,request, *args, **kwargs):
        data={
            "name":request.POST.get('name'),
            "email":request.POST.get('email'),
            "phone":request.POST.get('phone'),
            "sex":request.POST.get('sex'),
            "age":request.POST.get('age'),
            "address":request.POST.get('address'),
            "saved_by":request.user,
        }
        print(data.get("sex"))
        try :
            created=Customer.objects.create(**data)
            if created:
                messages.success(request,"Customer created successfully")
                
            else:
                messages.error(request,"Failed to create customer")
                
        except Exception as e:
            messages.error(request,f"Sorry our system is detecting the following issues {e}")
            
        return render(request,self.templates_name)
        
        
    