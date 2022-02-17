from django.shortcuts import redirect, render
from .models import *
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

# Create your views here.

def login(request):
    if request.POST:
        try:
            uid = User.objects.get(mobile = request.POST['mobile'])
            if uid.password == request.POST['password']:
                request.session['uid'] = uid.id
                return render(request,'account.html',{'uid':uid})
            else:
                return render(request,'login.html',{'msg':'Password Is wrong'})
        except:
            return render(request,'login.html',{'msg':'You do not have an account.'})
    return render(request,'login.html')

def registration(request):
    if request.POST:
        try:
            User.objects.get(mobile = request.POST['mobile'])
            return render(request,'registration.html',{'reg_msg':'You have already account'})
        except:
            User.objects.create(
                name = request.POST['name'],
                mobile = request.POST['mobile'],
                ver_code = request.POST.get('vcode',None),
                password = request.POST['password'],
                cpassword = request.POST['cpassword']
            )
            return render(request,'registration.html',{'reg_msg':'Account Created'})
    return render(request,'registration.html')

def logout(request):
    del request.session['uid']
    return redirect('login')

def index(request):
    return render(request,'index.html')

def account(request):
    return render(request,'account.html')


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def recharge(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'recharge.html', context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            # if result is None:
            amount = 20000  # Rs. 200
            try:

                # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)

                uid = User.objects.get(id=request.session['uid'])
                uid.rechage = 200
                uid.save()
                # render success page on successful caputre of payment
                return render(request, 'paymentsuccess.html')
            except:

                # if there is an error while capturing payment.
                return render(request, 'paymentfail.html')
            # else:
 
            #     # if signature verification fails.
                # return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()