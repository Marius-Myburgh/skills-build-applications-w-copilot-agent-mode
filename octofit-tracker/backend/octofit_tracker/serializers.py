
from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = '__all__'

    def get__id(self, obj):
        return str(obj._id) if obj._id else None

    def get_user(self, obj):
        return str(obj.user._id) if hasattr(obj.user, '_id') else str(obj.user) if obj.user else None

class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = '__all__'

    def get__id(self, obj):
        return str(obj._id) if obj._id else None

    def get_user(self, obj):
        # Return user id as string if present
        return str(obj.user._id) if hasattr(obj.user, '_id') else str(obj.user) if obj.user else None

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = '__all__'

    def get__id(self, obj):
        return str(obj._id) if obj._id else None

    def get_user(self, obj):
        # Return username if available, else fallback to id
        if hasattr(obj.user, 'name'):
            return obj.user.name
        elif hasattr(obj.user, 'email'):
            return obj.user.email
        elif hasattr(obj.user, '_id'):
            return str(obj.user._id)
        return str(obj.user) if obj.user else None
