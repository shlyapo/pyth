import datetime
import logging
from django.contrib.auth import authenticate
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
import asyncio

from first.models import User, Company, Employee, Salary


class SalaryListTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='username5',
            email='username5@gmail.com',
            first_name='Bob',
            password='123456',
            age=10,
            passport_numer=323434,
            passport_series='HB',

        )
        self.company=Company.objects.create(
            name="BelarusBank",
        )
        self.cl = Employee.objects.create(
            user=self.user
        )
        self.cl.companies.add(self.company)

        self.salary=Salary.objects.create(
            profession="Man",
            sum=300,
            company_id=self.company.id,
            employee_id=self.cl.id,
            date_salary=datetime.datetime.now(),
            is_now=False
        )

    def test_accounts_list_view_create_page_status_code_unauthenticated(self):
        response = self.employee.get(reverse("salaries"))
        self.assertEqual(response.status_code, 302)

    def test_accounts_create_page_status_code_authenticated(self):
        self.employee.force_login(user=self.user)
        response = self.employee.get(reverse("salaries"))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Managet')
        self.assertContains(response, 300)



