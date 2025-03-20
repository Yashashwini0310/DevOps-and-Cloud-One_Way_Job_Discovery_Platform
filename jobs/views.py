"""Create Views"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm

def home(request):
    return HttpResponse("Welcome to the Job Portal!")

def job_list(request):
    jobs = Job.objects.all()
    return render(request, "jobs/job_list.html", {"jobs": jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "jobs/job_detail.html", {"job": job})

@login_required
def job_create(request):
    """creating a Job object using a JobForm"""
    # Only logged-in users can create jobs
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = JobForm()
    return render(request, "jobs/job_form.html",{"form": form})

@login_required
def job_update(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = JobForm(instance=job)
    return render(request, "jobs/job_form.html", {"form": form})

def job_delete(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        job.delete()
        return redirect("job_list")
    return render(request, "jobs/job_confirm_delete.html", {"job": job})
