from django.urls import path

from . import views

urlpatterns = [
    path('validar-gru/', views.ListValidateGRUView.as_view(), name="list-validate-gru"),
    path('validar-gru/<int:pk>', views.ValidateGRUView.as_view(), name="validate-gru"),
    path('make-purchase/', views.MakePurchaseView.as_view(), name="make-purchase")
]
