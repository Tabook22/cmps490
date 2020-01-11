from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Place,GustComment
from .forms import PlaceForm, ImgForm

def index(request):
    pl_data=Place.objects.all()
    context={
        'pllst':pl_data,
        }
    return render(request,"place/place.html",context)

#add new comments------------------------------------------------------------------------
def addcomment(request):
    getpostid=""
    if request.method=="POST":
        getCom=GustComment(); #create instance of the model GustComment
        getCom.comtitle=request.POST.get("comtitle")
        getCom.comments=request.POST.get("comment")
        getCom.plname=Place.objects.get(id=int(request.POST.get("did")))
        getCom.save()
        getpostid=request.POST.get("did") #this is to get the post id

    #get all the comments about the same post
   #getcomments=GustComment.objects.all().filter(plname=getpostid)


    return redirect('main:detail',id=getpostid) #render(request,"index.html")
    #return redirect('main:detail', kwargs={'id':getpostid})
    #return redirect(reverse('main:detail', kwargs={'id':getpostid,'allcom':getcomments}))

#----------------------------------------------------------------------------------------
def search(request):
    #checking to see if the request method is post or get
    if request.method =="POST":
        #search the database for the places with the name stored inside the argument "plname" which comes with post
        plt=request.POST.get('pltitle')
        #getstn= places.objects.all()[:1].get() #getting the first record
        getplt=Place.objects.get(pltitle=plt)

    #return HttpResponse("<h1>" + getstn.stname + "</h1>")
    return render(request,"place/search.html",{'result':getplt})

#edit place here it will open the edit_st.html to display the data which will be modified
def editpl(request, id):
    getpl=Place.objects.get(id=id)

    return render(request,"place/edit_pl.html",{'result':getpl})
    #return HttpResponse("<h1>" + getst.stname + "</h1>")

#upload images
def uploadimg(request):
    form = ImgForm()
    return render(request,"uploadimg.html", {'form' : form})

#this will send the modified data to the be saved in the databae
def edit_pl(request):
    msg=""
    if request.method=="POST":
        pl=request.POST.get('id') #getting the id of the Place which will be saved. the id will be sent inside a hidden filed from the form
        getplaces=Place.objects.get(id=pl)
        getplaces.pltitle=request.POST.get('pltitle')
        getplaces.plid=request.POST.get('plid')
        getplaces.plstext=request.POST.get('plstext')
        getplaces.plstate=request.POST.get('plstate')
        getplaces.pllat=request.POST.get('pllat')
        getplaces.pllang=request.POST.get('pllang')

        getplaces.save()

        msg="places data updates successfully"
    else:
        msg="places data not update please see the administrator"

    pl_data=Place.objects.all()
    context={
        'pllst':pl_data,
        'msg':msg
        }
    return render(request,"place/place.html",context)

def delete(request, id):
    # id is the place id, we we get it from the form index.html
    # here we must check to see if the place with the id is there in the database or not
    obj=get_object_or_404(places,id=id)
    if obj:
        obj.delete()
        msg="places Deleted!"
    else:
        msg="places Not Deleted"

    pl_data=Place.objects.all()
    context={
        'pllst':pl_data,
        'msg':msg
        }
    return render(request,"place/place.html",context)

#Add New place ----------------------------------------------------------------
def add_new_pl(request):
    #getting the list of all places
    #pl_data=places.objects.all()
    #form = PlaceForm(request.POST or None)
    form=PlaceForm()
    #check to see if the request method is post or not
    if request.method=="POST":
        # Getting the posted data (the Place name and Place title )
        plt=request.POST.get("pltitle")
        pname=request.POST.get("pname")
        pls=request.POST.get("plstext")
        plst=request.POST.get("plstate")
        pll=request.POST.get("pllat")
        plla=request.POST.get("pllang")

        # adding data to the model
        place=Place(pltitle=plt, pname_id=pname, plstext=pls, plstate=plst, pllat=pll, pllang=plla  )
        place.save()
        context= {'form': form}
        return render(request, "place/place.html", context)
    else:
        #Here we are importing a form

        context= {'form': form}
        return render(request, "place/place.html", context)


#def delete(request, id):
  #  pass
