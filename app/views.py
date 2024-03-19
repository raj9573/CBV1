from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView,ListView,DetailView
from app.models import *


def FBV(request):

    return render(request,'first.html')


#Class Based VIews

class CBV(TemplateView): #Template View
    template_name = 'first.html'



def liststudents(request):

    SO = student.objects.all()


    return render(request,'students_lists.html',{'SO':SO})

#List View
class StudentsList(ListView):

    template_name = 'students_lists.html'

    model = student

    context_object_name = 'SO'



def StudentDetailFBV(request,pk):

    SO = student.objects.get(pk=pk)

    return render(request,'student_detail.html',{'SO':SO})





#DetailView
class StudentDetail(DetailView):

    template_name = 'student_detail.html'

    model = student

    context_object_name = 'SO'


