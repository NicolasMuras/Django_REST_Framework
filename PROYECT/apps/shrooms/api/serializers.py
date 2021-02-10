from rest_framework import serializers
from apps.shrooms.models import Shroom

#############################################[  GLOBALS  ]############################################

colors = ['Red', 'Orange', 'Blue', 'Yellow', 'White', 'Green', 'Gray', 'Black', 'Cyan']

##############################################[  MAIN  ]##############################################

class ShroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shroom
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'Especie': instance['specie'],
            'Dias_de_vida': instance['days'],
            'Color_del_sombrero': instance['cap_color'],
            'Color_del_tronco': instance['trunk_color']
        }

##############################################[ DETAIL ]##############################################

class DetailShroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shroom
        fields = '__all__'

##############################################[ CREATE ]##############################################

class CreateShroomSerializer(serializers.Serializer):

    specie = serializers.CharField(max_length = 50)
    days = serializers.IntegerField()
    cap_color = serializers.CharField(max_length=20)
    trunk_color = serializers.CharField(max_length=20)
    secret = serializers.CharField(max_length=10)

    def validate_specie(self, value):
        # custom validation
        if value == '':
            raise serializers.ValidationError('El campo esta vacio.')

        if 'Shroom' in value:
            raise serializers.ValidationError('Especie invalida.')

        return value

    def validate_days(self, value):
        # custom validation
        if value > 55 or value < 0:
            raise serializers.ValidationError('El rango de dias es invalido')

        return value

    def validate_cap_color(self, value):
        if value in colors:
            return value
        raise serializers.ValidationError('Color invalido.')

    def validate_trunk_color(self, value):
        if value in colors:
            return value
        raise serializers.ValidationError('Color invalido.')

    def validate(self, data):
        return data

    def create(self, validated_data):
        return Shroom.objects.create(**validated_data)

##############################################[ UPDATE ]##############################################

class UpdateShroomSerializer(serializers.Serializer):

    specie = serializers.CharField(max_length = 50)
    days = serializers.IntegerField()
    cap_color = serializers.CharField(max_length=20)
    trunk_color = serializers.CharField(max_length=20)
    secret = serializers.CharField(max_length=10)

    def validate_specie(self, value):
        if value == '':
            raise serializers.ValidationError('El campo esta vacio.')

        if 'Shroom' in value:
            raise serializers.ValidationError('Especie invalida.')

        return value

    def validate_days(self, value):
        # custom validation
        if value > 55 or value < 0:
            raise serializers.ValidationError('El rango de dias es invalido')
        
        return value

    def validate_cap_color(self, value):
        print(value)
        if value in colors:
            return value
        raise serializers.ValidationError('Color invalido.')

    def validate_trunk_color(self, value):
        print(value)
        if value in colors:
            return value
        raise serializers.ValidationError('Color invalido.')

    def validate(self, data):
        print(data)
        return data

    def update(self, instance, validated_data):
        print(validated_data)
        instance.specie = validated_data.get('specie', instance.specie)
        instance.days = validated_data.get('days', instance.days)
        instance.cap_color = validated_data.get('cap_color', instance.cap_color)
        instance.trunk_color = validated_data.get('trunk_color', instance.trunk_color)
        instance.save()
        return instance