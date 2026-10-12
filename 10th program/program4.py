
from django.shortcuts import get_object_or_404, redirect
from .models import Student

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return redirect('student_list')
