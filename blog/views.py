from django.shortcuts import render


# Create your views here.
rooms =[
    {'id': 1, 'name':'Compilation of Exercises'},
    {'id': 2, 'name':'About the Student'},
]


def home(request):
    context = {'rooms':rooms}
    return render(request, 'blog/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room' :room}
    
    return render(request, 'blog/room.html', context)

def about(request):
    return render(request, 'blog/about.html')
