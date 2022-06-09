import logging

from django.contrib.auth import authenticate, login
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from employee.models import Money
from .forms import LoginForm, UserRegistrationForm, CustomUserCreationForm
from .models import Employee, Manager, Accountant, User

logger = logging.getLogger('main')

class StartPageView(View):
    template_name = 'first/base.html'

    def get(self, request):
        return render(request, self.template_name)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'first/registration/signup.html'

    def form_valid(self, form):
        current_user = form.save()
        get_user=User.objects.filter(pk=current_user.id).first()
        client=Employee()
        client.user=get_user
        money=Money.objects.create(employee_id=get_user.id)
        money.employee=client
        money.save()
        #salary_list=SalaryList.objects.create()
        #salary_list.save()
        client.save()
        return super().form_valid(form)


class LoginView(View):
    template_name = 'first/registration/login.html'

    def post(self, request):
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                manager_exists = Manager.objects.filter(user=user).exists()
                if manager_exists:
                    return render(request, 'first/manager/manager_start.html', context={'manager': user})
                acc_exists = Accountant.objects.filter(user=user).exists()
                if acc_exists:
                    return render(request, 'first/accountant/accountant_start.html', context={'accountant': user})
                emp_exists = Employee.objects.filter(user=user).exists()
                if emp_exists:
                    return render(request, 'first/employee/employee_start.html', context={'employee': user})
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

class RegistrationView(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'first/registration/register.html', {'user_form': user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'first/registration/register_done.html', {'new_user': new_user})



