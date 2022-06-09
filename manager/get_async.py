from asgiref.sync import sync_to_async

from first.models import Employee, Salary


@sync_to_async
def get_company_employees(company):
     return Employee.objects.filter(companies__name=company)

@sync_to_async
def salary_comp(company):
     return Salary.objects.filter(company_id=company.id)
