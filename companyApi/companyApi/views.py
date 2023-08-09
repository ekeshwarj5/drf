from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page requested")
    employes=[
        'Ekeshwar',
        'Mayur',
        'Mayank'
    ]
    return JsonResponse(employes,safe=False)
