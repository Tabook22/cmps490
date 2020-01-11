from django.db import models
from pho.models import Photographer

# Create your models here.
class Place(models.Model):
    plname=models.CharField(verbose_name="Title Name", max_length=100,null=True, blank=True)
    plstext=models.CharField(verbose_name="Stext", max_length=100,null=True, blank=True)
    plstate=models.CharField(verbose_name="State", max_length=100,null=True, blank=True)
    pllat=models.CharField(verbose_name="Lat", max_length=100,null=True, blank=True)
    pllang=models.CharField(verbose_name="Lang", max_length=100,null=True, blank=True)
    pldesc=models.TextField(verbose_name="Description",null=True, blank=True)


    def __str__(self):
        return self.plname

class Image(models.Model):
    imgname=models.CharField(verbose_name="Image Name", max_length=200,null=True, blank=True)
    pname=models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name="pho_data")
    #uploadImg=models.ImageField(upload_to = 'pic_folder/%Y/%m/%d/%H/%M/%S/', default = 'pic_folder/None/no-img.jpg')
    uploadImg=models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    plname=models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place_data")
    desc=models.TextField(max_length=100,null=True, blank=True)
    status=models.BooleanField(default=False)
    main_img=models.BooleanField(default=False)

    def __str__(self):
        return self.imgname


class GustComment(models.Model):
    comtitle=models.CharField(verbose_name="Comment Title",max_length=200, null=True, blank=True)
    comments=models.TextField(verbose_name="Comments",null=True, blank=True)
    status=models.BooleanField(default=False)
    plname=models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.comtitle

class Comment(models.Model):
    ctitle=models.CharField(verbose_name="Title", max_length=200,null=True, blank=True)
    cdetail=models.TextField(verbose_name="Detail",null=True, blank=True)
    plname=models.ForeignKey(Place, on_delete=models.CASCADE)
    pname=models.ForeignKey(Photographer, on_delete=models.CASCADE, default=3)

    def __str__(self):
        return self.ctitle