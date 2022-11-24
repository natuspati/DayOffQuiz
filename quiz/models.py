from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

from versatileimagefield.fields import VersatileImageField, PPOIField


def team_directory_path(instance, filename):
    return 'team_{0}/{1}'.format(instance.name, filename)


class Team(models.Model):
    name = models.CharField(max_length=50)
    logo = VersatileImageField(
        upload_to=team_directory_path, ppoi_field="ppoi", null=True, blank=True
    )
    ppoi = PPOIField(null=True, blank=True)
    points = models.FloatField(null=True, default=0)
    
    def __str__(self):
        return "Team: %s" % self.name


class Venue(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return "Venue: %s" % self.name


class Event(models.Model):
    # Hidden fields
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    # Displayed fields
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    poster = VersatileImageField(
        upload_to="posters", ppoi_field="ppoi", null=True, blank=True
    )
    ppoi = PPOIField(null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateTimeField()
    teams = models.ManyToManyField(Team, through='Participation')
    price = models.IntegerField(validators=[MinValueValidator(0)])
    
    def __str__(self):
        return "Event: %s" % self.title


class Participation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.FloatField(null=True)
    
    def __str__(self):
        return "Team %s in event %s" % (self.team, self.event)


class Round(models.Model):
    game = models.ForeignKey(Participation, on_delete=models.CASCADE)
    score = models.FloatField(null=True, default=0)


class Revenue(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)
    expected = models.IntegerField(null=True)
    participated = models.IntegerField(null=True)
    value = models.IntegerField(null=True)
    
    def __str__(self):
        return "Event %s had revenue: %d" % (self.event, self.value)


class Player(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return "Player: %s in team %s" % (self.name, self.team)
