from django import forms
from .models import Place, Image

class PlaceForm(forms.ModelForm):
    class Meta:
        model=Place
        #fields = '__all__'
        fields=['plname','plstext','plstate','pllat','pllang','pldesc']


class ImgForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['imgname','pname','plname','uploadImg','status', 'desc','main_img']