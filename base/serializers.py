from rest_framework import serializers


class ResetPasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        password1 = data["password1"]
        password2 = data["password2"]
        if password1 == password2:
            return data
        else:
            raise ValueError("Passwords don't match")
