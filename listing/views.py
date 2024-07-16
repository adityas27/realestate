from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Property, Picture, Location, ImportantFigures, ContactForm
from users.models import Profile
from django.core import serializers
import json
from django.core.serializers import serialize

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
            Picture.objects.create(for_list=property, user=request.user, image=image)
    return render(request, 'add_carousel.html', {'property':property})

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
        data = 'Property Added Successfully'
        return HttpResponse(data)
@csrf_exempt
def del_wishlist(request):
    if request.method == 'POST':
        id = request.POST['id']
        print(id)
        profile = Profile.objects.get(user=request.user)
        if id in profile.wishlist:
            profile.wishlist.remove(id)
            data = {
            'message': 'Removed from wishlist',
            }
        else:
            data = {
            'message': 'No such property found',
            }
        profile.save()
        wishs = []
        for i in profile.wishlist:
            prop = Property.objects.get(id=i)
            wishs.append({'address_1': prop.location.address_1,
                          'address_2':prop.location.address_2,
                          'address_3': prop.location.address_3,
                          'address_4': prop.location.address_4,
                          'pincode': prop.location.pincode,
                          'id':prop.id,
                          'beds': prop.dimensions.beds,
                          'baths': prop.dimensions.baths,
                          'garage': prop.dimensions.garage,})
        
    return JsonResponse({
        'data': wishs
    }, safe=False)

def get_wishlist(request):
    prof = Profile.objects.get(user=request.user)

    wishs = []
    if prof.wishlist:
        for i in prof.wishlist:
            prop = Property.objects.get(id=i)
            wishs.append({'address_1': prop.location.address_1,
                            'address_2':prop.location.address_2,
                            'address_3': prop.location.address_3,
                            'address_4': prop.location.address_4,
                            'pincode': prop.location.pincode,
                            'id':prop.id,
                            'beds': prop.dimensions.beds,
                            'baths': prop.dimensions.baths,
                            'garage': prop.dimensions.garage,})
    return render(request, 'wishlist.html', {'wishs':wishs})

def contact_prop(request):
    if request.method == 'POST':
        id = request.POST['id']
        message = request.POST['message']
        prop = Property.objects.get(id=id)
        ContactForm.objects.create(prop=prop, message=message, email=request.user.email, ph_number=8451092347)
        return HttpResponse('Contact request sent successfully')

def mark_done(request):
    if request.method == 'POST':
        id = request.POST['id']
        details = ContactForm.objects.get(id=id)
        details.done = True
        details.save()
        return HttpResponse('Marked done')

def get_contacts(request):
    if request.user.is_superuser:
        tobecontacted = ContactForm.objects.filter(done=False)
        return render(request, 'contact_list.html', {'tobecontacted':tobecontacted})
    else:
        return HttpResponse('THIS PAGE IS ONLY FOR STAFF')