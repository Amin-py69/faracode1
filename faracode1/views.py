from django.shortcuts import render
from projects_app.models import Projects
from contactus_app.models import ContactUs, Message


def home(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        body = request.POST.get('body')

        Message.objects.create(fname=fname, email=email, sub=sub, body=body)

    project = Projects.objects.all()
    contact = ContactUs.objects.all().last()
    return render(request, 'index.html', context={'project': project, 'contact': contact})
