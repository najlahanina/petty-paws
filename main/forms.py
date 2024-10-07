from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class  ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "image", "brands", "price", "categories", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_image(self):
        image = self.cleaned_data["image"]
        return strip_tags(image) 
    
    def clean_brands(self):
        brands = self.cleaned_data["brands"]
        return strip_tags(brands)
    
    def clean_categories(self):
        categories = self.cleaned_data["categories"]
        return strip_tags(categories)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    

    