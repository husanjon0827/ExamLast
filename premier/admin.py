from django.contrib import admin

from premier.models import (
    User,
    League,
    Round,
    Team,
    LatestScores,
    Scheduled,
    Form,
    Statistics,
    News,
    Country,
    Leagues,
    LeaguesHokey,
    Teams,
    TeamsHokey,
    Matches,
    MatchesHokey,
)

admin.site.register(
    [
        User,
        League,
        Round,
        Team,
        LatestScores,
        Scheduled,
        Form,
        Statistics,
        News,
        Country,
        LeaguesHokey,
        Teams,
        TeamsHokey,
        Leagues,
        Matches,
        MatchesHokey,
    ]
)
