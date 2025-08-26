from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

Student = get_user_model()

class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Student.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the fields we don't need
        for field in ['username', 'student_number']:
            if field in self.fields:
                del self.fields[field]

    def validate(self, attrs):
        from django.contrib.auth import authenticate

        email = attrs.get('email')
        password = attrs.pop('password', None)

        if not email or not password:
            raise serializers.ValidationError('Must include email and password')

        try:
            user = Student.objects.get(email=email)
        except Student.DoesNotExist:
            raise serializers.ValidationError('Invalid email or password')

        # Authenticate using email and password
        user = authenticate(username=user.email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid email or password')

        if not user.is_active:
            raise serializers.ValidationError('User account is disabled')

        refresh = self.get_token(user)

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        }
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token
        token['department'] = user.department
        return token