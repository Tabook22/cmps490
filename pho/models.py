from django.db import models

# Create your models here.
class Photographer(models.Model):
    pname=models.CharField(verbose_name="photographer Name", max_length=100,null=True, blank=True)
    address=models.CharField(verbose_name="Address", max_length=100,null=True, blank=True)
    email=models.CharField(verbose_name="Email", max_length=100,null=True, blank=True)
    mobile=models.CharField(verbose_name="Mobile", max_length=100,null=True, blank=True)
    facebook=models.CharField(verbose_name="Facebook", max_length=100,null=True, blank=True)
    twitter=models.CharField(verbose_name="Twitter", max_length=100,null=True, blank=True)
    instagram=models.CharField(verbose_name="Instagram", max_length=100,null=True, blank=True)
    desc=models.TextField(verbose_name="Description", null=True, blank=True)
    uploadImg=models.ImageField(upload_to = 'pic_pho/', default = 'pic_pho/None/no-img.jpg')


    def __str__(self):
        return self.pname


class Uploadimg(models.Model):
    imgtitle=models.CharField(verbose_name="Title", max_length=200, null=True, blank=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    pname=models.ForeignKey(Photographer, on_delete=models.CASCADE)
    imgupload=models.ImageField(upload_to ='pic_folder')

    def __str__(self):
        return self.imgtitle