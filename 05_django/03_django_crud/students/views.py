from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

# index 페이지 - 학생들 목록
def index(request):
    students = Student.objects.all()[::-1]
    context = {'students':students}
    return render(request, 'students/index.html', context)

# CREATE
def new(requset):
    return render(requset, 'students/new.html')

def create(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')

    student = Student(name=name, age=age, email=email)
    student.save()

    return redirect('students:detail', student.pk)

# detail 페이지 - 학생 상세정보 
def detail(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    context = {'student':student}
    return render(request, 'students/detail.html', context)

# DELETE
# delete 페이지
def delete(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    student.delete()
    return redirect('students:index')

# UPDATE
def edit(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    context = {'student':student}
    return render(request, 'students/edit.html', context)

def update(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.email = request.POST.get('email')
    
    student.save()

    return redirect('students:detail', student_pk)