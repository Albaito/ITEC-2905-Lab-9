''' handles requests to homepage '''
from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import newPlaceForm

def place_list(request):


    if request.method == 'POST':
        form = newPlaceForm(request.POST)
        place = form.save() 
        if form.is_valid(): # checks if entered data meets DB constraints
            place.save()    # saves to DB
            return redirect('place_list')
        
    # if not POST, or form is invalid, renderss page with form to add new place, and list of places
    places = Place.objects.filter(visited=False).order_by('name')   # .filter() = SQL where
    new_place_form = newPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'new_place_form' : new_place_form})


def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited' : visited })


def place_was_visited(request, place_pk):
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()
    
    return redirect('place_list')