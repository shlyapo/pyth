from django.urls import path

from . import views
from .views import SalaryCreateView, AddMoneyView, EmployeeWork

urlpatterns = [
    path('', views.ManagerPageView.as_view(), name='home_manager'),
    path('salary/', views. SalaryListView.as_view(), name='salary'),
    path('salary/<int:pk>/update', views.SalaryUpdateView.as_view(), name='update'),
    path('salary/<int:pk>/delete', views.SalaryDeleteView.as_view(), name='delete'),
    path('project', views.ProjectView.as_view(), name='project'),
    path('project/confirm/<int:pk>', views.ApplyProjectView.as_view(), name="confirm"),
    path('project/delete_proj/<int:pk>', views.ProjectDeleteView.as_view(), name="delete_proj"),
    path('project/create', SalaryCreateView.as_view(), name="create"),
    path('money_add/', AddMoneyView.as_view(), name="money_add"),
    path('list_employee/', EmployeeWork.as_view(), name="list_employee"),
]