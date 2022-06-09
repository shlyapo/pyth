import asyncio

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
import employee.models
from first.views import logger
from manager.forms import SalaryForm
from manager.get_async import get_company_employees
from .models import *
from first.models import *
from manager.models import EmployeeProject


class EmployeePageView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = 'first/employee/employee_page.html'

    def get(self, request):
        first_name = User.first_name

        return render(request, self.template_name, context={'employee': request.user})


class SelectView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Company
    template_name = 'first/employee/company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_employee = Employee.objects.get(user=self.request.user)
        emp_comp = current_employee.companies.all()
        banks_without_acc = []
        company = Company.objects.all()
        for comp in company:
            if ( comp in emp_comp) == False:
                banks_without_acc.append(comp)
        context['banks_without_acc'] = banks_without_acc
        #context['all_banks'] = all_banks
        return context


class ProjectView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Company
    template_name = 'first/employee/salary_my.html'
    context_object_name = 'salary'

    def get_queryset(self):
        current_employee = Employee.objects.get(user=self.request.user)
        #client_list = SalaryList.objects.get(id=current_employee.salary_list.id)
        #salary=client_list.salarys.all()
        logger.info("salary")
        #return salary


class ApplyView(LoginRequiredMixin,ListView):
    login_url = 'login'
    template_name = 'first/employee/apply.html'
    context_object_name = 'comp_name'

    def get_queryset(self):
        current_employee = Employee.objects.get(user=self.request.user)
        company = Company.objects.get(pk=self.kwargs['pk'])
        #for emp_proj in EmployeeProject.objects.all():
           # if emp_proj.comp_id == self.kwargs['pk'] and emp_proj.emp_id == current_employee.id:
               # return company.name
        EmployeeProject.objects.create(comp_id=self.kwargs['pk'], emp_id=current_employee.id)
        logger.info("apply")
        return company.name


