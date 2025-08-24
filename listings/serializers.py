from rest_framework import serializers
from . models import Category,Property,PropertyImage
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=("id","name","slug")
        read_only_fields=("slug",)
class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model= PropertyImage
        fields=("id","image","is_cover","order")
class PropertySerializer(serializers.ModelSerializer):
    owner= serializers.ReadOnlyField(source="owner.username")
    image=PropertyImageSerializer(many=True,required=False)
    category= serializers.SlugRelatedField(slug_field="slug",queryset=Category.objects.all(),allow_null=True)
    class Meta:
        model = Property
        fields=("id","title","slug","description","price","city","address","area_sqm","bedrooms","bathrooms",
                "parking","year_built","property_type","status","is_published","features","created_at","updated_at",
                "owner","category","images")
        read_only_fields=("slug","owner","created_at","updated_at")
        def create(self,validated_data):
            images_data = validated_data.pop("images",[])
            property_obj= Property.objects.create(owner=self.context["request"].user,**validated_data)
            for img in images_data:
                PropertyImage.objects.create(property=property_obj,**img)
            return property_obj
        def update (self, instance, validated_data):
            images_data=validated_data.pop("images",None)
            for  attr ,value in validated_data.items():
                setattr(instance,attr,value)
            instance.save()
            if images_data is not None:
                instance.images.all().delete()
                PropertyImage.objects.create(property=instance,**img)
                return instance