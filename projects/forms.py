from django.forms import ModelForm 
from .models import Project, Review
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        # fields='__all__'
        fields=['title','featured_image','description','demo_link','source_link']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }
    def __init__(self ,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input'})

        for name,field  in self.fields.items():
            field.widget.attrs.update({'class':'input'})
    
    def clean_featured_image(self):
        image = self.cleaned_data.get('featured_image')
        if image:
            # Check file size (10MB limit)
            if image.size > 8 * 1024 * 1024:
                raise forms.ValidationError("Image file size must be under 8MB.")
            
            # Check file type
            allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']
            if hasattr(image, 'content_type') and image.content_type not in allowed_types:
                raise forms.ValidationError("Please upload a valid image file (JPEG, PNG, GIF).")
        
        return image


class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['value','body']

        labels={
            'value':'Place your Vote',
            'body':'Add a comment with your vote'
        } 

    def __init__(self ,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        

        for name,field  in self.fields.items():
            field.widget.attrs.update({'class':'input'})
