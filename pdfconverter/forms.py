from django import forms
# from .models import uploadfolder

CHOICES = [
    ('pdf2image','PDF to Image'),
    ('pdf2text','PDF to Text'),
    # ('pdf2docx','PDF to Docx'),
]

class displayform(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    func = forms.CharField(label='Select Option',widget = forms.RadioSelect(choices=CHOICES))
    # class Meta:
    #     model=uploadfolder
    #     fields=('File_to_upload',)
    #     widgets={ 
    #         'files' : forms.FileInput( attrs = { 'id':'files','required':True,'multiple':True } )
    #         }

class contactform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=1000)
    message = forms.CharField(widget= forms.Textarea)