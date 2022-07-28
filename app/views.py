from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        name = request.POST['message-name']
        email = request.POST['message-email']
        phone = request.POST['message-phone']
        message = request.POST['message']
        send_mail(
            'Message from ' + name +
            '(nr.tel.: ' + phone + '| email: ' + email + ')',  # subiect
            message,  # mesaj
            email,  # from email
            ['suport.marut@gmail.com', 'gabrieldan2399@gmail.com',
                'razvan_felecan@yahoo.com'],  # to email
        )
        return render(request, "base.html", {})
    else:
        return render(request, "base.html", {})


def about(request):
    return render(request, "about.html", {})


def services(request):
    return render(request, "services.html", {})


def products(request):
    return render(request, "products.html", {})


def blog(request):
    return render(request, "blog.html", {})


def contact(request):
    return render(request, "contact.html", {})


def windows(request):
    return render(request, "windows.html", {})


def doors(request):
    return render(request, "doors.html", {})


def rulouri(request):
    return render(request, "rulouri.html", {})


def accesories(request):
    return render(request, "accesories.html", {})
