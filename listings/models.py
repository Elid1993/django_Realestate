from django.db import models
from django.conf import settings
from slugify import slugify

class Category(models.Model):
    name= models.CharField(max_length=120,unique=True)
    slug= models.SlugField(max_length=150,unique=True,blank=True)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug =slugify(self.name)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name
    
class Property(models.Model):
    STATUS_CHOICES=(
        ("draft","Draft"),
        ("published","Published"),
        ("archived", "Archived"),
    )
    PROPERTY_TYPES=(
        ("apartment","Apartment"),
        ("house","House"),
        ("vila","Vila"),
        ("office","Office"),
        ("land","Land"),
        ("shop","Shop"),
    )    
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="properties")
    category= models.ForeignKey(Category,on_delete= models.SET_NULL ,null=True,related_name="properties")
    title= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200,unique=True,blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=12,decimal_places=0)
    city= models.CharField(max_length=120)
    address= models.CharField(max_length=255)
    area_sqm= models.PositiveIntegerField(help_text=("Enter the area in square meters"))
    bedrooms= models.PositiveSmallIntegerField(default=0)
    bathrooms=models.PositiveSmallIntegerField(default=0)
    parking= models.BooleanField(default=False)
    year_built= models.PositiveSmallIntegerField(null=True,blank=True)
    property_type= models.CharField(max_length=30,choices=PROPERTY_TYPES)
    status =models.CharField(max_length=20,choices=STATUS_CHOICES,default="draft")
    is_published= models.BooleanField(default=False)
    features= models.JSONField(default=dict,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["-created_at"]
        indexes=[
            models.Index(fields=["slug"]),
            models.Index(fields=["city","price"]),
        ]
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug= slugify(f"{self.title}-{self.city}-{self.owner_id}")
        super().save(*args,**kwargs)
    def __str__(self):
        return self.title
class PropertyImage(models.Model):
    property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name="images")
    image=models.ImageField(upload_to="properties/%y/%m/%d")
    is_cover =models.BooleanField(default=False)
    order= models.PositiveSmallIntegerField(default=0)
    class Meta:
        ordering =["order","id"]
    def __str__(self):
        return f"Image #{self.id}for {self.property_id}"