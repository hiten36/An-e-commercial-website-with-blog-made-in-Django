from django.shortcuts import render
from django.http import HttpResponse
from .models import product,contact,order,orderupdate
from math import ceil
import json
from django.contrib import messages

# Create your views here.
def index(request):
    prods=product.objects.all()
    n=len(prods)
    ns=n//4+ceil((n/4)-(n//4))
    l=[]
    catprods=product.objects.values('prod_cat','id')
    cat={item['prod_cat'] for item in catprods}
    for cats in cat:
        prod=product.objects.filter(prod_cat=cats)
        l.append([n,range(1,ns),prod])
    params={'list':l}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact1(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contacts=contact(name=name,email=email,phone=phone,desc=desc)
        contacts.save()
        messages.success(request,"Your feedback has been submitted.We'll get back to you ASAP!")
    return render(request,'shop/contact.html')

def tracker(request):
    if request.method=='POST':
        orderid=request.POST.get('order1','')
        email=request.POST.get('email','')
        try:
            orders=order.objects.filter(order_id=orderid,email=email)
            if len(orders)>0:
                update=orderupdate.objects.filter(order_id=orderid)
                updates=[]
                for i in update:
                    updates.append({'text':i.update_desc,'time':i.ts})
                    # response=json.dumps(updates,default=str)
                updates.append({'items':orders[0].items_json})
                response=json.dumps(updates,default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'shop/tracker.html')
def searchmatch(query,item):
    if query.lower() in item.prod_desc.lower() or query in item.prod_name.lower() or query in item.prod_cat.lower() or query in item.prod_sub_cat.lower():
        return True
    l=query.split(' ')
    l1=item.prod_name.split(' ')
    l2=item.prod_desc.split(' ')
    l3=item.prod_cat.split(' ')
    l4=item.prod_sub_cat.split(' ')
    if len(l)>1:
        for i in l:
            for j in l1:
                if i.lower() == j.lower():
                    return True
        for i in l:
            for j in l2:
                if i.lower() == j.lower():
                    return True
        for i in l:
            for j in l3:
                if i.lower() == j.lower():
                    return True
        for i in l:
            for j in l4:
                if i.lower() == j.lower():
                    return True
    return False

def search(request):
    query=request.GET.get('search')
    prods=product.objects.all()
    n=len(prods)
    ns=n//4+ceil((n/4)-(n//4))
    l=[]
    catprods=product.objects.values('prod_cat','id')
    cat={item['prod_cat'] for item in catprods}
    for cats in cat:
        prodtemp=product.objects.filter(prod_cat=cats)
        prod=[item for item in prodtemp if searchmatch(query,item)]
        if(len(prod))!=0:
            l.append([n,range(1,ns),prod])
    params={'list':l,'flag':False,'query':query}
    if len(l) == 0:
        params={'list':l,'flag':True,'query':query}
    return render(request,'shop/search.html',params)

def products(request,myid):
    prod=product.objects.filter(id=myid)
    prod1=product.objects.filter(id=myid).first().prod_cat
    prod2=product.objects.filter(prod_cat=prod1)
    n=len(product.objects.filter(prod_cat=prod1))
    nslides=n//4+ceil((n/4)-(n//4))
    l=[[n,range(1,nslides),prod2]]
    return render(request,'shop/products.html',{'prods':prod,'prodid':myid,'list':l})

def checkout(request):
    if request.method=='POST':
        json=request.POST.get('json','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip=request.POST.get('zip','')
        price=request.POST.get('price','')
        address=request.POST.get('address','')+' '+request.POST.get('address2','')
        orders=order(items_json=json,name=name,email=email,phone=phone,city=city,state=state,zip_code=zip,address=address,price=price)
        orders.save()
        update=orderupdate(order_id=orders.order_id,update_desc="The order has been placed.")
        update.save()
        with open('shop/a.txt','w') as f:
            f.write(str(orders.order_id))
        f.close()
    with open('shop/a.txt') as f:
        ids=int(f.read())+1
    f.close()
    return render(request,'shop/checkout.html',{'order_id':ids})
