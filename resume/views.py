from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Resume
from users.models import User
from .form import UpdateResumeForm


def update_resume(request):
    if request.user.is_applicant:
        resume = Resume.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateResumeForm(request.POST, request.FILES, instance=resume)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(pk=request.user.id)
                user.has_resume = True
                user.save()
                var.save()
                messages.info(request,' Your resume info has been updated.')
                return redirect('dashboard')
            else:
                messages.warning(request,'something went wrong')
        else:
            form = UpdateResumeForm(instance=resume)
            context = {'form': form}
            return render(request, 'resume/update_resume.html', context)
    else:
        messages.warning(request,'Permission denied')
        return redirect('dashboard')
    

def resume_details(request, pk):
    resume = Resume.objects.get(pk=pk)
    context = {'resume': resume}
    return render(request, 'resume/resume_details.html', context)