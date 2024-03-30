from django.db.models import (
    Model,
    DateField,
    CharField,
    ImageField,
    ManyToManyField,
    TextField,
    ForeignKey,
    CASCADE,
    DateTimeField,
)
from django.forms import IntegerField


class AbstractModel(Model):
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractModel):
    username = CharField(max_length=128)
    password = CharField(max_length=128)

    def __str__(self):
        return self.username


# football start
class League(AbstractModel):
    name = CharField(max_length=128)
    cover = ImageField(upload_to="media", default="media/default.jpg")

    def __str__(self):
        return self.name


class Round(AbstractModel):
    name = CharField(max_length=128)
    number = IntegerField()

    def __str__(self):
        return self.name


class Team(AbstractModel):
    name = CharField(max_length=128)
    stadium = CharField(max_length=128)
    capacity = IntegerField()
    cover = ImageField(upload_to="media", default="media/default.jpg")

    def __str__(self):
        return self.name


class LatestScores(AbstractModel):
    team_id = ManyToManyField("Team", related_name="latest_scores")
    league_id = ManyToManyField("League", related_name="latest_scores")
    round_id = ManyToManyField("Round", related_name="latest_scores")
    score = IntegerField()

    def __str__(self):
        return self.team_id


class Scheduled(AbstractModel):
    team_id = ManyToManyField("Team", related_name="scheduled")
    league_id = ManyToManyField("League", related_name="scheduled")
    round_id = ManyToManyField("Round", related_name="scheduled")

    def __str__(self):
        return self.team_id


class Form(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Statistics(AbstractModel):
    team_id = ManyToManyField("Team", related_name="statistics")
    mp = IntegerField()
    w = IntegerField()
    d = IntegerField()
    l = IntegerField()
    gd = IntegerField()
    pts = IntegerField()

    def __str__(self):
        return self.team_id


class News(AbstractModel):
    league_id = ManyToManyField("League", related_name="news")
    title = CharField(max_length=128)
    body = TextField()
    cover = ImageField(upload_to="media", default="media/default.jpg")

    def __str__(self):
        return self.title


class Country(AbstractModel):
    name = CharField(max_length=128)
    league_id = ManyToManyField("League", related_name="country")

    def __str__(self):
        return self.name


# football end
# start basketball
class Leagues(Model):
    name = CharField(max_length=128)
    cover = ImageField(upload_to="media", default="media/default.jpg")
    start_year = IntegerField()
    end_year = IntegerField()

    def __str__(self):
        return self.name
#A

class Teams(Model):
    name = CharField(max_length=128)
    stadium = CharField(max_length=128)
    cover = ImageField(upload_to="media", default="media/default.jpg")
    league_id = ForeignKey("Leagues", CASCADE, related_name="teams")

    def __str__(self):
        return self.name


class Matches(Model):
    team_id = ManyToManyField("Team", related_name="matches")
    date = DateTimeField()

    def __str__(self):
        return self.team_id


# end basketball
# start hockey
class LeaguesHokey(Model):
    name = CharField(max_length=128)
    cover = ImageField(upload_to="media", default="media/default.jpg")
    start_year = IntegerField()
    end_year = IntegerField()

    def __str__(self):
        return self.name


class TeamsHokey(Model):
    name = CharField(max_length=128)
    cover = ImageField(upload_to="media", default="media/default.jpg")
    w = IntegerField()
    d = IntegerField()
    l = IntegerField()

    def __str__(self):
        return self.name


class MatchesHokey(Model):
    first_team = ForeignKey(
        TeamsHokey, on_delete=CASCADE, related_name="matches_as_first_team"
    )
    second_team = ForeignKey(
        TeamsHokey, on_delete=CASCADE, related_name="matches_as_second_team"
    )
    time = DateTimeField()

    def __str__(self):
        return self.first_team


# end hockey
