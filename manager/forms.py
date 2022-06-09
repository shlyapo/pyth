from django import forms
from first.models import Salary
from manager.models import Storage


class SalaryForm(forms.ModelForm):

    class Meta:
        model = Salary
        fields = ('profession', 'sum')


class MoneyForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = ('sum',)