from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Service
from .forms import ContactForm


def about(request):
    return render(request, 'about.html')

def contract(request):
    return render(request, 'contract.html')

def home(request):
    return render(request, 'home.html')



def newsletter(request):
    return render(request, 'newsletter.html')


def pricelist(request):
    services = Service.objects.all()
    return render(request, 'pricelist.html', {'services': services})

def search_services(request):
    query = request.GET.get('query', '')
    services = Service.objects.filter(name__icontains=query)
    results = [
        {'name': service.name, 'description': service.description, 'estimated_days': service.estimated_days, 'cost': service.cost}
        for service in services
    ]
    return JsonResponse(results, safe=False)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page or back to the form
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')