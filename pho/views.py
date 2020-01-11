from django.shortcuts import render,redirect,get_object_or_404
from .models import Photographer

#the first welcome page
def index(request):
    p_data=Photographer.objects.all().order_by("pname")[:3]

    return render(request, "index.html", {'plst':p_data})
    #return redirect('/photo/cjsonfile/')
    #return render(request, "photo/index.html")

# search the website
def search(request):
    #checking to see if the request method is post or get
    if request.method =="POST":
        #search the database for the photographer with the name stored inside the argument "stname" which comes with post
        pn=request.POST.get('pname')
        #getstn= photographer.objects.all()[:1].get() #getting the first record
        getpn=Photographer.objects.get(pname=pn)

    #return HttpResponse("<h1>" + getstn.stname + "</h1>")
    return render(request,"pho/search.html",{'result':getpn})


#edit photographer here it will open the edit_st.html to display the data which will be modified
def editp(request, id):
    getp=Photographer.objects.get(id=id)

    return render(request,"pho/edit_p.html",{'result':getp})
    #return HttpResponse("<h1>" + getst.stname + "</h1>")


#this will send the modified data to the be saved in the databae
def edit_p(request):
    msg=""
    if request.method=="POST":
        p=request.POST.get('id') #getting the id of the student which will be saved. the id will be sent inside a hidden filed from the form
        getphotographer=Photographer.objects.get(id=p)
        getphotographer.pname=request.POST.get('pname')
        getphotographer.pid=request.POST.get('pid')
        getphotographer.pimage=request.POST.get('pimage')
        getphotographer.pstate=request.POST.get('pstate')
        getphotographer.porder=request.POST.get('porder')
        getphotographer.pstext=request.POST.get('pstext')

        getphotographer.save()

        msg="photographer data updates successfully"
    else:
        msg="photographer data not update please see the administrator"

    p_data=Photographer.objects.all()
    context={
        'plst':p_data,
        'msg':msg
        }
    return render(request,"pho/pho.html",context)


def delete(request, id):
    # id is the photographer id, we we get it from the form index.html
    # here we must check to see if the photographer with the id is there in the database or not
    obj=get_object_or_404(Photographer,id=id)
    if obj:
        obj.delete()
        msg="photographer Deleted!"
    else:
        msg="photographer Not Deleted"

    p_data=Photographer.objects.all()
    context={
        'plst':p_data,
        'msg':msg
        }
    return render(request,"pho/pho.html",context)

#Add New photographer
def add_new_p(request):
    #Here we are going to declare a variable to hold the message
    msg=""
    #check to see if the request method is post or not
    if request.method=="POST":
        # Getting the posted data (the student name and student collage)
        pn=request.POST.get("pname")
        pi=request.POST.get("pid")
        pim=request.POST.get("pimage")
        ps=request.POST.get("pstate")
        po=request.POST.get("porder")
        pst=request.POST.get("pstext")


        # adding data to the model
        pho=Photographer(pname=pn, pid=pi, pimage=pim, pstate=ps, porder=po, pstext=pst  )
        pho.save()
        msg="photographer data was saved"
    else:
        msg="photographer Data Not Saved!!"

    #here we are retrieving all the data from the student's table
    p_data=Photographer.objects.all()

    #here we are creating a dictionary to hold the retrived data and also the message
    context={
        'plst':p_data,
        'msg':msg
        }
    return render(request,"pho/pho.html",context)
