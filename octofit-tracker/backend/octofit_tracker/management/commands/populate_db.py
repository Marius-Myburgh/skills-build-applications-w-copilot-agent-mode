from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='thundergod', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='metalgeek', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='zerocool', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='crashoverride', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='sleeptoken', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        user_ids = [str(user._id) for user in users]
        blue_team = Team(_id=ObjectId(), name='Blue Team', members=user_ids)
        gold_team = Team(_id=ObjectId(), name='Gold Team', members=user_ids)
        blue_team.save()
        gold_team.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=60, date='2025-06-09T08:00:00Z'),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120, date='2025-06-09T09:00:00Z'),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=90, date='2025-06-09T10:00:00Z'),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=30, date='2025-06-09T11:00:00Z'),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=75, date='2025-06-09T12:00:00Z'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], points=100, rank=1),
            Leaderboard(_id=ObjectId(), user=users[1], points=90, rank=2),
            Leaderboard(_id=ObjectId(), user=users[2], points=95, rank=3),
            Leaderboard(_id=ObjectId(), user=users[3], points=85, rank=4),
            Leaderboard(_id=ObjectId(), user=users[4], points=80, rank=5),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), user=users[0], workout_type='Cycling Training', details='Training for a road cycling event', date='2025-06-09T13:00:00Z'),
            Workout(_id=ObjectId(), user=users[1], workout_type='Crossfit', details='Training for a crossfit competition', date='2025-06-09T14:00:00Z'),
            Workout(_id=ObjectId(), user=users[2], workout_type='Running Training', details='Training for a marathon', date='2025-06-09T15:00:00Z'),
            Workout(_id=ObjectId(), user=users[3], workout_type='Strength Training', details='Training for strength', date='2025-06-09T16:00:00Z'),
            Workout(_id=ObjectId(), user=users[4], workout_type='Swimming Training', details='Training for a swimming competition', date='2025-06-09T17:00:00Z'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
