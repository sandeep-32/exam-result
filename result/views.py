from django.shortcuts import render
from .models import StudentResult
from django.views.generic import TemplateView,ListView,DetailView
from django.db.models import Q
# Create your views here.(object)
class HomePageView(TemplateView):
    template_name='home.html'

class StudentListView(ListView):
    model=StudentResult
    template_name='student_list.html'
    context_object_name='studentlist'
    def get_queryset(self):
        query=self.request.GET.get("q")
        return StudentResult.objects.filter(Q(name__iexact=query) |Q(roll__iexact=query))





class StudentDetailResult (DetailView):
    model=StudentResult
    template_name='student_detail.html'
