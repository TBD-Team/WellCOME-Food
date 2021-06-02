from django.urls import path, include
from rest_framework import routers

from authentication import views as auth_views
from payment import views as payment_views

router = routers.DefaultRouter()
router.register(r'users', auth_views.UserViewSet)
#router.register(r'purchases', payment_views.PurchaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', auth_views.CustomAuthToken.as_view()),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restaurant/', include('restaurant.urls')),
    path('purchases/', payment_views.PurchaseAPIView.as_view()),
    path('credits/', payment_views.CreditAPIView.as_view())
]
