from django.shortcuts import render, reverse
from .models import Student
from .forms import StudentModelForm
from django.http import HttpResponseRedirect
from django.views.generic import View


def index(request):
    students = Student.get_all()
    if request.method == "POST":
        student_form = StudentModelForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect(reverse("index"))
    student_form = StudentModelForm()
    return render(request, "student/index.html", {"students": students, "student_form": student_form})


class IndexView(View):
    template_name = "student/index.html"

    def get_context_data(self):
        students = Student.get_all()
        return {"students": students}

    def get(self, request, *args, **kwargs):
        student_form = StudentModelForm()
        context = self.get_context_data()
        context.update({"student_form": student_form})
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        student_form = StudentModelForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect(reverse("index"))
        context = self.get_context_data()
        context.update({"student_form": student_form})
        return render(request, self.template_name, context)
