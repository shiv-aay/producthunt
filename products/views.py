from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from . import forms

# Create your views here.
def home(request):
    products= Product.objects.all()
    return render(request,'products/homepage.html',{'products':products})

def detail(request, product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})

@login_required(login_url="/accounts/login")
def create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.hunter=request.user
            instance.save()
            instance.upvoted_by.add(request.user)
            return redirect('home')
            return redirect('/products/'+str(product.id))
    else: form = forms.CreateArticle()
    return render(request,'products/create.html',{'form':form})

@login_required(login_url="/accounts/login")
def upvote(request,product_id):
    if request.method == 'POST':
        product=get_object_or_404(Product,pk=product_id)
        product.upvoted_by.add(request.user)
        return redirect('/products/'+str(product.id))
