
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            department=request.POST['department'],
            email=request.POST['email']
        )
        return redirect('student_list')

    return render(request, 'student_form.html')

def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.department = request.POST['department']
        student.email = request.POST['email']
        student.save()
        return redirect('student_list')

    return render(request, 'student_form.html',
                  {'student': student})
