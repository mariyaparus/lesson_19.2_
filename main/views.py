from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject


# Create your views here.
class StudentListView(ListView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Главная'})
        return context


# def index(request):
#     students_list = Student.objects.all()
#     context = {
#         'object_list': students_list,
#         'title': 'Главная'
#     }
#     return render(request, 'main/student_list.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contact.html', context)


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Студент'})
        return context


# def view_student(request, pk):
#     student_item = get_object_or_404(Student, pk=pk)
#
#     context = {
#         'object': student_item
#     }
#     return render(request, 'main/student_detail.html', context)

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    # fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Создание студента'})
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    # fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     SubjectFormSet = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
    #     if self.request.method == 'POST':
    #         context['formset'] = SubjectFormSet(self.request.POST, instance=self.object)
    #     else:
    #         context['formset'] = SubjectFormSet(instance=self.object)
    #     context.update({'title': 'Редактирование студента'})
    #     return context

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            formset = SubjectFormset(self.request.POST)
        else:
            formset = SubjectFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Удаление студента'})
        return context


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    context = {
        'object': student_item,
        'title': 'Активен?',
    }

    return redirect(reverse('main:index'), context)
