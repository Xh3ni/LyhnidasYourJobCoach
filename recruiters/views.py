from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Job, Applicants, Selected
from candidates.models import Profile, Skill
from .forms import NewJobForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def rec_details():
    context = {
        'rec_home_page': "active",
        'rec_navbar':1,
    }


def add_job(request):
    user = request.user
    if request.method == "POST":
        form = NewJobForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.recruiter = user
            data.save()
            return redirect('job-list')
    else:
        form = NewJobForm()
    context = {
        'add_job_page': "active",
        'form': form,
        'rec_navbar': 1,
    }
    return render(request, 'recruiters/add_job.html', context)



