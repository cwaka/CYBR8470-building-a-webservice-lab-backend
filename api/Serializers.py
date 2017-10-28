from rest_framework
from .models import Dog
from .models import Breed


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('name', 'age', 'gender', 'color', 'favoritefood', 'favoritetoy'. 'breed')

class BreedSerializer(serializers.ModelSerializer):

        class Meta:
            model = BreedSerializer
            fields = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')
