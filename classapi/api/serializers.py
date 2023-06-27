# create serializers here
from rest_framework import serializers
from api.models import classes,student
class classesserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=classes
        fields="__all__"


class studentserializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=student
        fields="__all__"