from django.views import View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from payment.models import Credit, Account


class CustomView(View):
    @method_decorator(login_required(login_url="/accounts/login", redirect_field_name=""))
    def dispatch(self, request):
        return super().dispatch(request)


class ListValidateGRUView(CustomView):

    def get(self, request):
        credits = Credit.objects.filter(status='AN')
        paginator = Paginator(credits, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "pages/list-validate-gru.html", {'page_obj': page_obj})


class ValidateGRUView(CustomView):

    def get(self, request):
        return render(request, "pages/validate-gru.html")

    def post(self, request, pk):
        pass


class MakePurchaseView(CustomView):
    def get(self, request):
        return render(request, "pages/make-purchase.html")

    def post(self, request):
        purchase_code = request.POST["purchase-code"]
        try:
            account = Account.objects.get(purchase_code=purchase_code)
            purchase = account.make_purchase()
        except Account.DoesNotExist:
            messages.error(request, "Conta com este código não existe")
        except Exception as e:
            messages.error(request, "Não tem saldo suficiente!")
        else:
            messages.success(request, "Compra efetuada!")
        return redirect('make-purchase')