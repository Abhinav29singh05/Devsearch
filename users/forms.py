from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill , Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
        labels={
            'first_name': 'Name',
        } 
        
    def __init__(self ,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input'})

        for name,field  in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        fields= ['name','email','username','location','bio','short_intro','profile_image','social_github','social_twitter','social_linkedin','social_website']
    
    def __init__(self ,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input'})

        for name,field  in self.fields.items():
            field.widget.attrs.update({'class':'input'})
    
    def clean_profile_image(self):
        image = self.cleaned_data.get('profile_image')
        if image:
            try:
                # Check file size (5MB limit)
                if image.size > 5 * 1024 * 1024:
                    raise forms.ValidationError("Image file size must be under 5MB.")
                
                # Check file type
                allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']
                if hasattr(image, 'content_type') and image.content_type not in allowed_types:
                    raise forms.ValidationError("Please upload a valid image file (JPEG, PNG, GIF).")
            except Exception as e:
                print(f"Error validating image: {str(e)}")
                raise forms.ValidationError("Error processing image file.")
        
        return image



class SkillForm(ModelForm):
    class Meta:
        model=Skill
        fields='__all__'
        exclude=['owner']


    def __init__(self ,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input'})

        for name,field  in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class MessageForm(ModelForm):
    class Meta:
        model=Message
        fields=['name','email','subject','body']

    def __init__(self ,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)

        
        for name,field  in self.fields.items():
            field.widget.attrs.update({'class':'input'})
