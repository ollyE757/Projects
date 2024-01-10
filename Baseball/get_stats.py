import pandas as pd


## Read in teams and data
data = pd.read_csv('stats/teams.csv')
data_dict = data.to_dict(orient='records')

teams = {}
for team in data_dict:
    teams.update({team['Name'] : team})

# print(teams)

## For each team get their stats into a dataframe and append to respecitve dicts
for team in teams:
    url = 'https://www.baseball-reference.com/teams/' + teams[team]['Acronym'] + '/2023.shtml'
    
    team_stats = pd.read_html(url)
    
    batting_stats = team_stats[0]
    pitching_stats = team_stats[1]

    teams[team]['Batting Stats'] = batting_stats
    teams[team]['Pitching Stats'] = pitching_stats

reds_batting = teams['Cincinnati Reds']['Batting Stats']
print(reds_batting.loc[reds_batting['Name'] == 'Matt McLain'][['Name', 'Age', 'PA', 'OPS']])