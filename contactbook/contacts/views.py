from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {'contacts': contacts})

def add_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']

        Contact.objects.create(
            name=name,
            phone=phone,
            email=email
        )
        return redirect('home')

    return render(request, 'contacts/add.html')

def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.save()
        return redirect('home')

    return render(request, 'contacts/edit.html', {'contact': contact})

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('home')
