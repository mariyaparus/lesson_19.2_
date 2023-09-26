from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Student


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
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Создание студента'})
        return context


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Редактирование студента'})
        return context


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
