from django.shortcuts import render,get_object_or_404

from place.models import Place, Image, GustComment
from pho.models import Photographer
# Create your views here.

def index(request):
    """ select the main image """
    main_img=Image.objects.values('uploadImg').filter(main_img=True)[0]['uploadImg']

    """select the title and the text of the main image """
    imgname=Image.objects.values('imgname').filter(main_img=True)[0]['imgname']
    desc=Image.objects.values('desc').filter(main_img=True)[0]['desc']

    #main_img=Image.objects.filter(main_img=True).only("uploadImg")


    pl_data=Image.objects.filter(status=True).select_related('plname','pname') [:6]
    context={
        'mimg':main_img,
        'imgname':imgname,
        'desc':desc,
        'plst':pl_data,
        }
    return render(request,"index.html",context)


#This will show the place full details
def detail(request,id):
    getlat=""
    getlang=""
    #here we are going to get details about the place who has an id=id
    getPlace=Place.objects.filter(id=id)

    #get latitude and longitude for the map
    for mp in getPlace:
        getlat=mp.pllat
        getlang=mp.pllang

    #here we are going to get all the comments about that place
    getComm=GustComment.objects.filter(plname=id,status=True).order_by('-id') [:4]

    #here we are getting the image of the require place
    for i in getPlace:
        getImg=Image.objects.filter(plname=i.id)

    #place_detail = Image.objects.all().select_related('plname')
    #place_detail.filter(id=id)

    #this is for displaying maps
    mapbox_access_token = 'pk.eyJ1IjoidGFib29rMjIiLCJhIjoiY2s0djcycHk3MGQ4YzNscjg5cm50M3QzaiJ9.u3bnVXXsHSRGAgShQwe5Qg'
    #return render(request, 'default.html',
                  #{ 'mapbox_access_token': mapbox_access_token })

    #here we put all the details inside a dictionary called context
    context={
        'lat':getlat,
        'lang':getlang,
        'id':id,
        'getimg':getImg,
        'pldetail':getPlace,
        'getc':getComm,
        'mapbox_access_token': mapbox_access_token
        }
    return render(request,"details.html", context)

def pho_detail(request, id):
    getPho=Photographer.objects.filter(id=id)

    context={
        'phodetail':getPho
        }
    return render(request,"pho.html", context)

