from django.urls import path

from . import views
from .views import AccountantPageView, SalaryListView, ApplyProjectView, StaticMoneyView

urlpatterns = [
    path('',  AccountantPageView.as_view(), name='home'),
    path('salary_list/', SalaryListView.as_view(), name='salary_list'),
    path('apply_salary/<int:pk>', ApplyProjectView.as_view(), name='apply_salary'),
    path('money_trans/', StaticMoneyView.as_view(), name='money_trans'),
    path('null_salary', SalaryListView.as_view(), name='null_salary'),
    #path('logout-then-login/', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
]