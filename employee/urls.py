from django.urls import path

from . import views
from .views import EmployeePageView, ProjectView, SelectView, ApplyView

urlpatterns = [
    path('', EmployeePageView.as_view(), name='employee'),
    #path('salary_my/', ProjectView.as_view(), name="salary_my"),
    path('company/', SelectView.as_view(), name='company'),
    path('apply/<int:pk>', ApplyView.as_view(), name='apply'),
    #path('money/', MoneyView.as_view(), name='money'),
]