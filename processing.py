#!/usr/bin/env python3

import os
import pandas as pd

DATA = pd.read_csv(os.path.join('92-to-23_results/premier-league-matches.csv'))
YEARS = list(set(DATA['Season_End_Year']))

def get_data():
    """
    returns the data stored in the csv file
    """
    return DATA

def getTable(season_end_year: int, wk=42):
    """
    Returns the premier league table for the season.

    Optionally, it can return the table at the end of a specific gameweek too
    """
    if wk is not None:
        # If week is provided, check if it's an integer
        if not isinstance(wk, int):
            raise ValueError("Parameter 'x' must be an integer.")

    # a table with the seasons results    
    results = DATA[(DATA['Season_End_Year'] == season_end_year) & (DATA['Wk'] <= wk)]
    teams = list(set(results['Home']))

    table = []
    for team in teams:
        homegames = results[results['Home'] == team]
        awaygames = results[results['Away'] == team]

        games_played = len(homegames) + len(awaygames)
        games_won = len(homegames[homegames['FTR'] == 'H']) + len(awaygames[awaygames['FTR'] == 'A'])
        games_drawn = len(homegames[homegames['FTR'] == 'D']) + len(awaygames[awaygames['FTR'] == 'D'])
        games_lost = len(homegames[homegames['FTR'] == 'A']) + len(awaygames[awaygames['FTR'] == 'H'])

        goals_scored = sum(homegames['HomeGoals'])+sum(awaygames['AwayGoals'])
        goals_conceded = sum(homegames['AwayGoals'])+sum(awaygames['HomeGoals'])
        goal_diff = goals_scored - goals_conceded

        points = (games_won * 3) + games_drawn

        table.append({'Team': team,
                      'Played': games_played,
                      'Won': games_won, 
                      'Drawn': games_drawn,
                      'Lost': games_lost, 
                      'GF': goals_scored, 
                      'GA': goals_conceded, 
                      'GD': goal_diff, 
                      'Points': points
                      })
        
    table = pd.DataFrame(table).sort_values(by='Points', ascending=False)
    table.index = range(1, len(table) + 1)
    
    return table


def relegated():
    pass

def promoted():
    pass

def getTotalWins():
    pass

def talking():
    return 'Hello'