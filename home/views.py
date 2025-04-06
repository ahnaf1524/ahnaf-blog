from django.shortcuts import render,HttpResponse
from .models import Contact
# Create your views here.
def home(request):
    return render(request , 'home/home.html')
def about(request):
    return render(request , 'home/about.html')
def contact(request):
    if request.method == "POST":
        try:
            full_name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            if not full_name or not email or not message:
                raise ValueError("Required fields missing")
            # Save to DB
            contact_entry = Contact(
                full_name=full_name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            contact_entry.save()

            return render(request, 'home/contact.html', {'success': True})
        
        except Exception as e:
            return render(request, 'home/contact.html', {'error': str(e)})

    return render(request, 'home/contact.html')