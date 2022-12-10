from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from home.models import *
from events.models import *
from coordinator.models import *
from users.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token



JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class SponsorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = '__all__'

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BrochureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brochure
        fields = '__all__'

class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class PanelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = '__all__'

class EventSponsorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EventSponsors
        fields = '__all__'

class StreamLinksSerializers(serializers.ModelSerializer):
    class Meta:
        model = StreamLinks
        fields = '__all__'

class CoodinatorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coordinator
        fields = '__all__'

class CarouselSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = '__all__'

class ThemeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class SubmissionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Submissions
        fields = '__all__'

# class CustomUserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ExtendedUser
#         fields = '__all__'

class ExtendedUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = '__all__'
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        user = ExtendedUser
        user.set_password(validated_data['password'])
        user.save()

        return user

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class PreRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PreRegistration
        fields = '__all__'

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        else :
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        
        return {
            'email':user.email,
            'token': jwt_token
        }