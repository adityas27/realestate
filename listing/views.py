from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse
from .models import Property, Picture, Location, ImportantFigures
from users.models import Profile
from django.core import serializers
import json
from django.core.serializers import serialize
# Create your views here.
def index(request):
    return render(request, 'landing_page.html')

def listing(request):
    props = Property.objects.all()
    pics = Picture.objects.all()
    return render(request, 'index.html', {'props': props, 'pics':pics})

@csrf_protect 
@login_required
def add_prop(request):
    if request.method == 'POST':
        # getting data from form
        form = request.POST #text data
        image = request.FILES.get('images') #file data
        form.dict() # converging form to dict
        #saving location
        address_1 = form['address_1']
        address_2 = form['address_2']
        address_3 = form['address_3']
        address_4 = form['address_4']
        pincode = form['pincode']
        city = form['city']
        state = form['state']
        nation = form['nation']
        location = Location.objects.create(address_1=address_1, address_2=address_2, address_3=address_3, address_4=address_4,
            pincode=pincode, city=city, state=state, nation=nation)
        location.save()

        # saving dimensions
        area = form['area']
        lot_area = form['lot_area']
        no_of_floors = form['no_of_floors']
        ground_to_floor = form['ground_to_floor']
        beds = form['beds']
        baths = form['baths']
        garage = form['garage']

        details = ImportantFigures.objects.create(area=area, lot_area=lot_area, no_of_floors=no_of_floors, ground_to_floor=ground_to_floor, beds=beds, baths=baths, garage=garage)
        details.save()

        # saving property
        price = form['price']
        year_built = form['year_built']
        furnished = bool(form['furnished'])
        prop_type = form['house_type']
        own_type = form['own_type']
        desc = form['desc']
        hidden = bool(form['hidden'])

        
        prop = Property.objects.create(location=location,dimensions=details, price=price, year_built=year_built,prop_type=prop_type, own_type=own_type, desc=desc, furnished=furnished, hidden=hidden, thumbnail=image)
        prop.save()

        return redirect('add')
    else:
        return render(request, 'add_property.html')
    
def detail(request, prop_id):
    property = get_object_or_404(Property, id=prop_id)
    pictures = list(Picture.objects.filter(for_list=prop_id))
    return render(request, 'details.html', {'property':property, 'pictures':pictures})

def addPics(request, prop_id):
    property = get_object_or_404(Property, id=prop_id)
    if request.method == 'POST':
        images = request.FILES.getlist('images') #file data
        for image in images:
            img = Picture.objects.create(for_list=property, user=request.user, image=image)
            print('saved ', img.for_list)
    
    return render(request, 'add_carousel.html', {'property':property})

@login_required
def add_wishlist(request):
    if request.method == 'POST':
        id = request.POST['id']
        profile = Profile.objects.get(user=request.user)
        if profile.wishlist != None:
            if id in profile.wishlist:
                return HttpResponse('Already in wishlist')
            profile.wishlist.append(id)
        else:
            profile.wishlist=[]
            profile.wishlist.append(id)
        profile.save()
        data = {
            'message': 'Property Successfully added to wish list',
            # Add other data you want to return
        }
        return HttpResponse(data)
    
@login_required
def del_wishlist(request):
    if request.method == 'POST':
        id = request.POST['id']
        print(request.POST['id'])
        profile = Profile.objects.get(user=request.user)
        # if id in profile.wishlist:
        #     profile.wishlist.remove(id)
        #     data = {
        #     'message': 'Removed from wishlist',
        #     }
        # else:
        #     data = {
        #     'message': 'No such property found',
        #     }
        # profile.save()
        wishs = []
        for i in profile.wishlist:
            prop = Property.objects.get(id=i)
            print(prop)
            wishs.append(prop)
            
            # print(prop.location.pincode)
        print(wishs[0].location.pincode)
        print(wishs)
        queryset_json = serialize('json', wishs)
        print(queryset_json[0])
        queryset_data = json.loads(queryset_json)
    return JsonResponse(queryset_data, safe=False)

def get_wishlist(request):
    prof = Profile.objects.get(user=request.user)
    wishs = []
    for i in prof.wishlist:
        prop = Property.objects.get(id=i)
        wishs.append(prop)
    queryset_json = serialize('json', wishs)
    queryset_data = json.loads(queryset_json)
    return JsonResponse(queryset_data, safe=False)