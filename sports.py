import json
import requests
from pycricbuzz import Cricbuzz
from datetime import datetime, timedelta

def currentFootballMatches():
    yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    tomorrow = datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d')
    url = "https://apifootball.com/api/?action=get_events&from="+yesterday+"&to="+tomorrow+"&league_id=62&APIkey=87a80add20d9445cd383d8c5ec37bb1ff04906beb59297e57bc1abea06c61fc7"
    response = requests.get(url)
    data = json.loads(response.text)
    map = {}
    for match in data:
        if match['match_live'] == '1':
            map['status'] = 'true'
            map['between'] = match['match_awayteam_name'] + " and " + match['match_hometeam_name']
            map['scores'] = match['match_awayteam_name'] + " scored " + match['match_awayteam_score'] + " while " + match['match_hometeam_name'] + " scored " + match['match_hometeam_score'] + " goals."
            awayScorers = ''
            homeSocrers = ''
            for scorer in match['goalscorer']:
                if scorer['home_scorer'] != None:
                    homeSocrers = homeSocrers + scorer['home_scorer'] + " scored a goal at " + scorer['time']
                else:
                    awayScorers = awayScorers + scorer['away_scorer'] + " scored a goal at " + scorer['time']
            map['homeScorers'] = homeSocrers
            map['awayScorers'] = awayScorers
            statistic = ''
            for stat in match['statistics']:
                statistic = statistic + stat['type'] + " by " + match['match_hometeam_name'] + " is " + stat['home'] + " and " + match['match_awayteam_name'] + " is " + stat['away'] + ". "
            map['statistics'] = statistic
        else:
            map['status'] = 'false'
    return map

def cricketMatches():
    c = Cricbuzz()
    matches = c.matches()
    arr = []
    for match in matches:
        if match['mchstate'] == 'inprogress':
            map = {}
            liveScore = getLiveScore(match['id'])
            map['between'] = match['team1']['name'] + " and " + match['team2']['name']
            map['location'] = match['venue_name'] + " in " + match['venue_location']
            map['series'] = match['srs']
            map['status'] = match['status']
            map['score'] = liveScore
            arr.append(map)
    return arr

def getLiveScore(matchId):
    c = Cricbuzz()
    scores = c.livescore(matchId)
    data = ''
    data = data + " Team " + scores['batting']['team'] + " is currently batting. Score stands at " + scores['batting']['score'][0]['runs'] + \
    " for " + scores['batting']['score'][0]['wickets'] + " in " + scores['batting']['score'][0]['overs'] + " overs. " + \
    scores['batting']['batsman'][0]['name'] + " is batting at " + scores['batting']['batsman'][0]['runs'] + " in " + \
    scores['batting']['batsman'][0]['balls'] + " and " + scores['batting']['batsman'][1]['name'] + " is batting at " + \
    scores['batting']['batsman'][1]['runs'] + " in " + scores['batting']['batsman'][1]['balls'] + ". " + \
    scores['bowling']['bowler'][0]['name'] + " from " + scores['bowling']['team'] + " is bowling his " + \
    scores['bowling']['bowler'][0]['overs'] + " overs and has given " + scores['bowling']['bowler'][0]['runs'] + \
    " runs and has taken " + scores['bowling']['bowler'][0]['wickets'] + " wickets."
    return data

if __name__ == '__main__':
    print("hello! Logs In sports")
#87a80add20d9445cd383d8c5ec37bb1ff04906beb59297e57bc1abea06c61fc7