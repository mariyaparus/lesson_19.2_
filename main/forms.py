from django import forms

from main.models import Student, Subject


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'  # Все поля
        fields = ('first_name', 'last_name', 'avatar',)  # Конкретные поля
        # exclude = ('is_active',)  # Исключить поля


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'
