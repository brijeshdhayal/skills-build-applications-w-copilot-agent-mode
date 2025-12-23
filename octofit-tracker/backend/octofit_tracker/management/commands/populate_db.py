from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=spiderman, type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Swimming', duration=25, date=timezone.now().date())
        Activity.objects.create(user=superman, type='Walking', duration=60, date=timezone.now().date())

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        situps = Workout.objects.create(name='Situps', description='Do 30 situps')
        pushups.suggested_for.add(marvel)
        situps.suggested_for.add(dc)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
