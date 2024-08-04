from django.shortcuts import redirect, render , HttpResponse
from app.models import Category, Order, Product,Contact_us,Brand
from django.contrib.auth import authenticate, login, logout
from app.models import UsercreateForm  # Ensure this import is correct
from django.views import View
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User
def Master(request):
    return render(request, 'master.html')

def Index(request):
    category = Category.objects.all()
    categoryID = request.GET.get('category')
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
            'category': category,
            'product': product,
            'brand' : brand,
        }
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UsercreateForm(request.POST)
        if form.is_valid():  
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('index')
    else:
        form = UsercreateForm()
    
    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)
    # return render(request, 'registration/signup.html')

# def login(request):
#     return render(request,'registration/login.html')
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')
    
@login_required(login_url="/accounts/login/")
def cart_add(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")

@login_required(login_url="/accounts/login/")
def item_clear(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/accounts/login/")
def item_increment(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/accounts/login/")
def item_decrement(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url="/accounts/login/")
def cart_detail(request):

    return render(request,'cart/cart_detail.html')

def Contact_Page(request):
    if request.method == "POST":
        contact = Contact_us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()
    return render(request,'contact.html')

def CheckOut(request):
    if request.method == "POST":
        address = request.POST.get('address'),
        phone = request.POST.get('phone'),
        pincode = request.POST.get('pincode'),
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)
        
        print(cart)
        for i in cart:
            a = int(cart[i]['price'])
            b = cart[i]['quantity']
            total = a*b
            order = Order(
                user = user,
                product  = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                total = total,
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
            )
            order.save()
        request.session['cart'] = {}
        return redirect('index')
        
    return render(request, 'checkout.html')
def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk = uid)
    order = Order.objects.filter(user = user)

    order = Order.objects.filter(user = user)

    context={
        'order':order,
    }
    return render(request,'order.html',context)

def Product_page(request):
    category = Category.objects.all()
    categoryID = request.GET.get('category')

    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        product = Product.objects.all()
    context = {
        'category':category,
        'brand':brand,
        'product':product,
    }
    return render(request,'product.html',context)


def Product_Detail(request,id):
    product  = Product.objects.filter(id = id).first()
    context = {

        'product' : product,
    }
    return render(request,'product_detail.html',context)

def Search(request):
    query = request.GET['query']

    product = Product.objects.filter(name__icontains = query)
    context = {
        'product': product,
    }
    return render(request,'search.html',context)
