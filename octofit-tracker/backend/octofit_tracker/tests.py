
from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="testpass")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(email="team@example.com", name="Team User", password="testpass")
        team = Team.objects.create(name="Test Team", members=[user])
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email="activity@example.com", name="Activity User", password="testpass")
        activity = Activity.objects.create(user=user, activity_type="run", duration=30, date="2025-06-09T00:00:00Z")
        self.assertEqual(activity.activity_type, "run")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email="workout@example.com", name="Workout User", password="testpass")
        workout = Workout.objects.create(user=user, workout_type="cardio", details="30 min run", date="2025-06-09T00:00:00Z")
        self.assertEqual(workout.workout_type, "cardio")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(email="leaderboard@example.com", name="Leaderboard User", password="testpass")
        leaderboard = Leaderboard.objects.create(user=user, points=100, rank=1)
        self.assertEqual(leaderboard.points, 100)
