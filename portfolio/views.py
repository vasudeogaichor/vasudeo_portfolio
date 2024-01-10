from django.shortcuts import redirect

def home(request):
    new_url = 'https://portfolio-nine-chi-60.vercel.app/'
    return redirect(new_url)

def blogs(request):
    new_url = 'http://13.201.32.219:3000/'
    return redirect(new_url)

def pnr(request):
    new_url = 'http://13.201.32.219:8000/'
    return redirect(new_url)