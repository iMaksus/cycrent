from dataclasses import fields
from rest_framework import serializers
from .models import Bicycle

# serializer helps convert the data from the API into a form, like JSON, that can be usable in the frontend. 
# create a serializer
class RecipeSerializer(serializers.ModelSerializer):
    # initialize model and fields you want to serialize
    class Meta:
        model = Bicycle
        fields = ('title', 'time_minutes', 'ingredients')