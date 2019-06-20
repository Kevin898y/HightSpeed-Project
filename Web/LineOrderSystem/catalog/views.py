from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import UsernameForm,CustomerForm

from django.shortcuts import render_to_response
import pandas as pd

Orders = pd.read_csv('Order.csv')
findOrder = []
  
def home(request):
    text = 'a' 
    date = ''
    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            # text = form.cleaned_data['Username']
            start_date = form.cleaned_data['start_date'].strftime('%Y-%m-%d')
            end_date = form.cleaned_data['end_date'].strftime('%Y-%m-%d')
            findsdate = Orders['Date']>=start_date
            findedate = Orders['Date']<=end_date
            # findname = Orders['Username']==text
            order = Orders[findsdate & findedate]
            order.sort_values(by = ['Date'],inplace = True)
            findOrder = []
            num=1
            for u,p,q,d in zip(order['Username'],order['Product'],order['Quantity'],order['Date']):
                findOrder.append( [u,p,q,d,num] )
                num+=1
          
            context = {
                'findOrder': findOrder,
            }
            return render(request,'order.html',context=context)
    else:
        form = UsernameForm() 
    context = {
        'form': form,
        'text':text,
        'date':date,
    }
    
    # return render_to_response('home.html')

    return render(request, 'home.html', context=context)

def customer(request):
    text = ''
    date = ''
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['Username']
            start_date = form.cleaned_data['start_date'].strftime('%Y-%m-%d')
            end_date = form.cleaned_data['end_date'].strftime('%Y-%m-%d')
            findsdate = Orders['Date']>=start_date
            findedate = Orders['Date']<=end_date
            findname = Orders['Username']==text
            order = Orders[findsdate & findedate& findname]
            findOrder = []
            num =1
            for u,p,q,d in zip(order['Username'],order['Product'],order['Quantity'],order['Date']):
                findOrder.append( [u,p,q,d,num] )
                num+=1
            context = {
                'findOrder': findOrder,
            }
            return render(request,'CustomerOrder.html',context=context)
            
    else:
        form = CustomerForm()
    context = {
        'form': form,
        'text':text,
        'date':date,
    }
    # return render_to_response('home.html')

    return render(request, 'customer.html', context=context)

def contact(request):
  
    return render(request, 'Contact.html')

def reference(request):
   
    return render(request, 'Reference.html')