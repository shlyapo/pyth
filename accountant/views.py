import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from accountant.models import SalaryProject
from employee.models import Money
from first.models import Salary
from first.models import Accountant, Company, User, Employee
from first.views import logger
from manager.models import Storage, TransMoney


class AccountantPageView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = 'first/accountant/accountant_page.html'

    def get(self, request):
        first_name = User.first_name

        return render(request, self.template_name, context={'accountant': request.user})


class SalaryListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'first/accountant/salary_list.html'
    context_object_name = 'salaries'

    def get_queryset(self):
        current_accountant = Accountant.objects.get(user=self.request.user)
        company = Company.objects.get(id=current_accountant.company.id)
        salary = Salary.objects.filter(company_id=company.id)
        salaries=[]
        logger.info("salary-list")
        for s in salary:
            time_salary=s.date_salary
            day=time_salary.day
            time_now=datetime.datetime.today()
            time_day=time_now.day
            if day is time_day and s.is_now is False:
                emp = Employee.objects.get(id=s.company.id)
                user = emp.user
                emp_sal = {"last_name": user.last_name, "salary": s.id,
                                "profession": s.profession, "sum": s.sum, "date_of_salary": s.date_salary}
                salaries.append(emp_sal)
        return salaries


class ApplyProjectView(LoginRequiredMixin, View):#######
    login_url = 'login'
    template_name = 'first/accountant/apply_salary.html'

    def get(self, request, pk):
        salary = Salary.objects.get(pk=pk)
        emp = Employee.objects.get(pk=salary.employee_id)
        comp = Company.objects.get(pk=salary.company_id)
        storage = Storage.objects.get(comp_id=comp.id)
        mon = storage.sum - salary.sum
        if mon>=0:
            salary.is_now=True
            storage.sum = storage.sum - salary.sum
            money=Money.objects.get(employee_id=emp.id)
            money.sum=money.sum+salary.sum
            status = "Add salary"
            trans_money = TransMoney.objects.create(sum=salary.sum, status=status, company=comp)
            trans_money.save()
            storage.save()
            logger.info("salary")
        #salary.delete()
            return render(request, self.template_name)
        return render(request, 'first/accountant/null_money.html')


class StaticMoneyView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'first/accountant/money_trans.html'
    context_object_name = 'trans'

    def get_queryset(self):
        current_accountant = Accountant.objects.get(user=self.request.user)
        current_company=Company.objects.get(id=current_accountant.company.id)
        #money=Storage.objects.get(id=current_company.storage.id)
        money_trans = TransMoney.objects.filter(company_id=current_company.id)
        trans = []
        for s in money_trans:
            emp_sal = {"status": s.status, "sum": s.sum,
                        "date": s.date_of_trans}
            trans.append(emp_sal)
        return trans

