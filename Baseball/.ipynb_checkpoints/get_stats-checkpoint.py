# import pandas as pd
# import matplotlib.pyplot as plt


# ## Read in teams and data
# data = pd.read_csv('stats/teams.csv')
# data_dict = data.to_dict(orient='records')

# teams = {}
# for team in data_dict:
#     teams.update({team['Name'] : team})

# # print(teams)

# ## For each team get their stats into a dataframe and append to respecitve dicts
# for team in teams:
#     url = 'https://www.baseball-reference.com/teams/' + teams[team]['Acronym'] + '/2023.shtml'
    
#     team_stats = pd.read_html(url)
    
#     batting_stats = team_stats[0]
#     pitching_stats = team_stats[1]

#     teams[team]['Batting Stats'] = batting_stats
#     teams[team]['Pitching Stats'] = pitching_stats

# # reds_batting = teams['Cincinnati Reds']['Batting Stats']
# # print(reds_batting.loc[reds_batting['Name'] == 'Matt McLain'][['Name', 'Age', 'PA', 'OPS']])
    
# teams['Chicago Cubs']['Batting Stats'].plot(kind='scatter',
#         x='H',
#         y='R',
#         colour='blue')

# plt.title('Hits vs. OPS')

# plt.show()





# importing required library
# In case pandas is not installed on your machine
# use the command 'pip install pandas'.
import pandas as pd
import matplotlib.pyplot as plt
 
# A dictionary which represents data
data_dict = {'name': ['p1', 'p2', 'p3', 'p4', 'p5', 'p6'],
             'age': [20, 20, 21, 20, 21, 20],
             'math_marks': [100, 90, 91, 98, 92, 95],
             'physics_marks': [90, 100, 91, 92, 98, 95],
             'chem_marks': [93, 89, 99, 92, 94, 92]
             }
 
# creating a data frame object
df = pd.DataFrame(data_dict)
 
# show the dataframe
# bydefault head() show
# first five rows from top
df.head()



# scatter plot
df.plot(kind='scatter',
        x='math_marks',
        y='physics_marks',
        color='red')
 
# set the title
plt.title('ScatterPlot')
 
# show the plot
plt.show()