import django_filters as df
from .models import Property
class PropertyFilter(df.FilterSet):
    min_price= df.NumberFilter(field_name="price",lookup_expr="gte")
    max_price=df.NumberFilter(field_name="price",lookup_expr="lte")
    min_area=df.NumberFilter(field_name="area_sqm",lookup_expr="gte")
    max_area= df.NumberFilter(field_name="area_sqm",lookup_expr="lte")
    class Meta:
        model =Property 
        fields =["city","property_type","is_published","status"]