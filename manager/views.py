import datetime

from first.views import logger
from multiprocessing.pool import ThreadPool
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
import asyncio
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
import collections
import multiprocessing
# Create your views here.
from first.models import Salary
from first.models import Manager, Company, Employee, User
from manager.forms import SalaryForm, MoneyForm
from manager.get_async import get_company_employees, salary_comp
from manager.models import EmployeeProject, Storage, TransMoney


class ManagerPageView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = 'first/manager/manager_page.html'

    def get(self, request):
        first_name = User.first_name

        return render(request, self.template_name, context={'manager': request.user})


class SalaryListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Salary
    template_name = 'first/manager/salary.html'
    context_object_name = 'salary_com'

    def get_queryset(self):
        current_manager = Manager.objects.get(user=self.request.user)
        current_company=Company.objects.get(id=current_manager.company.id)
        company = current_company.name
        comp_emps = get_company_employees(company)
        salary_of_company = Salary.objects.filter(company_id=current_company.id)
        proj = []
        for pr in salary_of_company:
            employee = Employee.objects.get(pk=pr.employee_id)
            user = employee.user
            employee_proj = {"last_name": user.last_name,
                             "profession": pr.profession, "sum": pr.sum, "date_of_salary": pr.date_salary,
                             "project": pr.id}
            proj.append(employee_proj)
        return proj




class SalaryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Salary
    template_name = 'first/manager/update.html'
    context_object_name = 'salary'
    fields = ('profession', 'sum',)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.id})


class SalaryCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    success_url = reverse_lazy("salary-list")

    def get(self, request):
        form = SalaryForm()
        current_manager = Manager.objects.get(user=self.request.user)
        current_company=Company.objects.get(id=current_manager.company.id)
        company=current_company.name
        comp_emps = get_company_employees(company)

        return render(self.request, 'first/manager/create.html',
                      {'form': form, 'comp_emps': asyncio.run(comp_emps)})

    def post(self, request):
        form = SalaryForm(self.request.POST)
        if form.is_valid():
            current_manager = Manager.objects.get(user=self.request.user)
            salary = form.save(commit=False)
            if 'dropdown' in self.request.POST:
                username = self.request.POST['dropdown']
                us=User.objects.get(username=username)
                current_employee = Employee.objects.get(user=us)
                salary.employee = current_employee
                current_company = Company.objects.get(id=current_manager.company.id)
                salary.company = current_company
                salary.save()

                logger.info("created")
                return render(self.request, 'first/manager/finish.html')
        current_manager = Manager.objects.get(user=self.request.user)
        current_company = Company.objects.get(id=current_manager.company.id)
        company = current_company.name
        comp_emps = get_company_employees(company)

        return render(self.request, 'first/manager/create.html',
                      {'form': form, 'comp_emps': asyncio.run(comp_emps)})


class SalaryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Salary
    template_name = 'first/manager/delete.html'
    context_object_name='salary'
    success_url = reverse_lazy("salary")


class EmployeeCompanyView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Employee
    template_name = 'first/manager/employee.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_manager = Manager.objects.get(user=self.request.user)
        current_company = Company.objects.get(pk=current_manager.company.id)
        emp = current_company.employee_set.all()
        context['emp'] = emp
        return context


class ProjectView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'first/manager/project.html'
    context_object_name = 'project'

    def get_queryset(self):
        current_manager = Manager.objects.get(user=self.request.user)
        company = Company.objects.get(pk=current_manager.company.id)
        projects = EmployeeProject.objects.filter(comp_id=company.id)
        proj=[]
        for pr in projects:
            employee = Employee.objects.get(pk=pr.emp_id)
            user=employee.user
            employee_proj= {"first_name": user.first_name, "last_name": user.last_name,
                            "passport_series": user.passport_series, "passport_numer": user.passport_numer,
                            "project": pr.id}
            proj.append(employee_proj)
        return proj


class ApplyProjectView(LoginRequiredMixin, View):#######
    login_url = 'login'
    template_name = 'first/manager/confirm.html'

    def get(self, request, pk):
        proj = EmployeeProject.objects.get(pk=pk)
        emp = Employee.objects.get(pk=proj.emp_id)
        comp = Company.objects.get(pk=proj.comp_id)
        # sal_list = SalaryList.objects.get
        emp.companies.add(comp)
        proj.delete()
        return render(request, self.template_name)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = EmployeeProject
    template_name = 'first/manager/delete_proj.html'
    success_url = reverse_lazy('project')
    context_object_name = 'project'


class AddMoneyView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    success_url = reverse_lazy("")###

    def get(self, request):
        current_manager = Manager.objects.get(user=self.request.user)
        company = Company.objects.get(pk=current_manager.company.id)
        selected = Storage.objects.get(comp_id=company.id)
        return render(self.request, 'first/manager/money_add.html', {'money': selected, 'message': ''})

    def post(self, request):
        sum = int(request.POST.get("sum"))
        current_manager = Manager.objects.get(user=self.request.user)
        company = Company.objects.get(pk=current_manager.company.id)
        selected = Storage.objects.get(comp_id=company.id)
        if sum <= 0:
            message = 'Putting money failed!'
            return render(self.request, 'first/manager/money_add.html', {'money': selected, 'message': message})
        else:
            selected.sum += sum
            selected.save()
            status = "Add money"
            trans_money = TransMoney.objects.create(sum=sum, status=status, company=company)
            trans_money.save()
            logger.info("add-money")
            return render(self.request, 'first/manager/money_finish.html')

class EmployeeWork(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Salary
    template_name = 'first/manager/list_employee.html'
    context_object_name = 'salary_com'

    def process_item(item):
        return {"profession": item.profession, 'time': datetime.datetime.today() - item.date_salary}

    def get_queryset(self):
        current_manager = Manager.objects.get(user=self.request.user)
        current_company = Company.objects.get(id=current_manager.company.id)
        comp_emps=Salary.objects.filter(company_id=current_company.id)
        pool = ThreadPool()
        res = pool.map_async(self.process_item, comp_emps)
        w = res.get()
        pool.close()
        #pool = multiprocessing.Pool()
        #result = pool.map(self.process_item, comp_emps)
        return w







