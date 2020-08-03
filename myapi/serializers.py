from rest_framework import serializers
from rest_framework.settings import api_settings
from .models import InternationalFinancialInstitute
from django.contrib.auth.models import User

class IFISerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = InternationalFinancialInstitute
        fields = ('name', 'legalAddress', 'responsiblePersonFullname', 'responsiblePersonPosition', 'responsiblePersonPhoneNumber', 'responsiblePersonEmail', 'additionalContactPersonFullname', 'additionalContactPersonPosition', 'additionalContactPersonPhoneNumber', 'additionalContactPersonEmail', 'owner')

class GetFullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_superuser', 'email')


class UserSerializerWithToken(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)
        return token
        
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'] 
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'email')
