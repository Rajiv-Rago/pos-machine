from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def openpos(request):
   items = item.objects.all()

   return render (request, 'newapp/openpos.html', {'items': items})

def item_list(request):
   items = item.objects.all()

   if(request.method == "POST"):
      ID = request.POST.get('ID')
      item.objects.filter(pk=ID).delete()
      print(ID)

   return render (request, 'newapp/item_list.html', {'items': items})

def add_item(request):
   if(request.method == "POST"):
      item_name = request.POST.get('item_name')
      item_price = request.POST.get('item_price')
      stock_quantity = request.POST.get('stock_quantity')

      item.objects.create(item_name = item_name, item_price = item_price, stock_quantity=stock_quantity)
      
      return redirect('item_list')
   
   else:
      return render(request, 'newapp/add_item.html')

def edit_item(request, pk):
   i = item.objects.filter(pk=pk)
   if(request.method == "POST"):
      item_name = request.POST.get('item_name')
      item_price = request.POST.get('item_price')
      stock_quantity = request.POST.get('stock_quantity')

      i.update(item_name=item_name, item_price=item_price, stock_quantity=stock_quantity)

      return redirect('item_list')

   else:
      return render (request, 'newapp/edit_item.html', {'item': i.get()})
   
def confirm_order(request):
   if(request.method == "POST"):
      ptype = request.POST.get("payment_method")
      items = request.POST.get("complete_order")
      totamt = request.POST.get("total_amount")
      ord = order.objects.create(total_amount_paid=totamt, payment_type=ptype)

      item_fixed = items[:-1]
      
      stuff = item_fixed.split("-")
      for it in stuff:
         it = it.split(":")
         item_obj = item.objects.get(pk=it[0])
         
         itprice = item_obj.getPrice()
         lt = itprice * int(it[1])

         
         item_order.objects.create(item = item_obj, order = ord, line_total=lt, quantity=it[1])

         i = item.objects.filter(pk=it[0])
         current_quantity = item_obj.getStockQuantity()
         i.update(stock_quantity=current_quantity - int(it[1])) 

   return redirect('openpos')