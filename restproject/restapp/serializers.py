from rest_framework import serializers
from .models import Student, Student1


#  using model-serializer with CRUD
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class Student1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = '__all__'
