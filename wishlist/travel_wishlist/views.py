''' handles requests to different pages present in urls.py '''
from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import newPlaceForm
from django.contrib.auth.decorators import login_required

@login_required
def place_list(request):

    '''
        If the request is a POST request, when the add button is clocked it'll validate the input,
        and save to DB, then redirect it the current page
    '''

    if request.method == 'POST':
        form = newPlaceForm(request.POST)
        place = form.save(commit=False) 
        place.user = request.user
        if form.is_valid(): # checks if entered data meets DB constraints
            place.save()    # saves to DB
            return redirect('place_list')
        
    # if not POST, or form is invalid, renderss page with form to add new place, and list of places
    # based upon which user is connected
    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name')   # .filter() = SQL where
    new_place_form = newPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places' : places, 'new_place_form' : new_place_form})

@login_required
def places_visited(request):
    visited = Place.objects.filter(user=request.user).filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited' : visited })

@login_required
def place_was_visited(request, place_pk):
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()
    
    return redirect('place_list')

@login_required
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    return render(request, 'travel_wishlist/place_detail.html', {'place' : place})