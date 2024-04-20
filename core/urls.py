from django.urls import path

from core import views
from core.views import CreateUser, AllTransactions, CheckBalance, CheckPassbook

urlpatterns = [
    path('register/', CreateUser.as_view()),
    path('balance/<int:account_number>', CheckBalance.as_view()),
    path('passbook/<int:account_number>', CheckPassbook.as_view()),
    path('payment/', AllTransactions.as_view()),
    path('hi/', views.landing_page, name='landing_page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
]
