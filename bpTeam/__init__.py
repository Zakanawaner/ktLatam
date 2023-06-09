from flask import Blueprint, render_template, current_app
from flask_login import current_user

from utils.team import getTeams, getTeam, getTeamOnly


teamBP = Blueprint('teamBluePrint', __name__)


@teamBP.route("/teams/<country>", methods={"GET", "POST"})
def teamsEndPoint(country):
    tms = getTeams(country)
    return render_template(
        'teams.html',
        title="Equipos",
        teams=tms,
        country=current_app.config['COUNTRIES'][country],
        user=current_user if not current_user.is_anonymous else None
    )


@teamBP.route("/team/<te>", methods={"GET", "POST"})
def teamEndPoint(te):
    team = getTeamOnly(te)
    teTor = getTeam(te)
    return render_template(
        'team.html',
        title=team.name,
        team=team,
        teTor=teTor,
        user=current_user if not current_user.is_anonymous else None
    )
