from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
     template = loader.get_template('index.html') 
     return HttpResponse(template.render())

def form(request):
     template = loader.get_template('form.html') 
     return HttpResponse(template.render())

# Create
def create_user(request):
     form = PersonForm()

     if request.method == 'POST':
          form = PersonForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('index_one')
          
     context ={'form':form}
     return render(request, 'form.html', context)

# Read
def read_user(request):
     person = Person.objects.all
     # form = PersonForm(instance=person)
     
     context ={'persons':person}
     return render(request, 'form.html', context)


# Update
def update_user(request, pk):
     person = Person.objects.get(id = pk)
     form = PersonForm(instance=person)

     if request.method == 'POST':
          form = PersonForm(request.POST, isinstance=person)
          if form.is_valid():
               form.save()
               return redirect('index_one')
     
     context ={'form':form}
     return render(request, 'form.html', context)

# Delete
def delete_user(request, pk):
     person = Person.objects.get(id = pk)
     if request.method == 'POST':
          person.delete()
          return redirect('index_one')

     context ={'form':form}
     return render(request, 'form.html', context)