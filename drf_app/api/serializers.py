from datetime import datetime

from rest_framework import serializers

from drf_app.models import Album, Track, Robot, RobotType, RobotCategory


class RobotSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Robot
        fields = '__all__'


class RobotTypeSerializer(serializers.ModelSerializer):
    model = RobotType
    fields = '__all__'


class RobotCategorySerializer(serializers.ModelSerializer):
    model = RobotCategory
    fields = '__all__'


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


comment = Comment(email='robot@hotmail.com', content='robot e-mail')


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=100)
    created = serializers.DateTimeField()