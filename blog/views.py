from django.shortcuts import render

def post_list(request):
    return render(request, 'blot/post_list.html', {})
