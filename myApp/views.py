from django.shortcuts import render

def post_list(request):
    return render(request, 'MyApp/post_list.html', {})