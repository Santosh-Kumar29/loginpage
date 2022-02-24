from rest_framework import serializers

from login_form.models import login_page
from .models import login_page


class logformserializer(serializers.ModelSerializer):
    class Meta:
        model = login_page
        fields = '__all__'


class logvieweserializer(serializers.ModelSerializer):
    class Meta:
        model = login_page
        fields = ('username', 'email_id', 'mobile_no', 'is_active')


class isactiveserializer(serializers.ModelSerializer):
    class Meta:
        model = login_page
        fields = ('username', 'is_active')