from django.shortcuts import render,redirect
from .models import Hotel,Category,Location
# Create your views here.
def hotel(request):
    photo = Hotel.objects.all()
    locations = Location.objects.all()
    return render(request,'hotel.html',{'images':photo,'locations':locations})
def display_location(request):
    try:
        location = Location.objects.get(id = location_id)
        photos = Hotel.objects.filter(image_location = location.id)
    except:
        raise Http404()
    return render(request,'loc.html',{'location':location,'images':images})
def display_categories(request):    
    images = Hotel.image_categories()

    return render(request, 'category.html', {"images":images}) 
def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Hotel.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
        return render(request, 'search.html', {'message':message})