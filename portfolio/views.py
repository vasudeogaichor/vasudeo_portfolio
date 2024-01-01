from django.shortcuts import redirect

def home(request):
    new_url = 'https://portfolio-nine-chi-60.vercel.app/'
    return redirect(new_url)

def blogs(request):
    new_url = 'http://54.234.18.211:3000'
    return redirect(new_url)