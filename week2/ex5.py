from operator import itemgetter

# The structure of a team is as follow:
# team_name: (points, wins, goals_for, goals_against, ties, losses)
POINTS = 0
WINS = 1
GOALS_FOR = 2
GOALS_AGAINST = 3
TIES = 4
LOSSES = 5


def win(teams, winner, loser):
    teams[winner][WINS] += 1
    teams[loser][LOSSES] += 1
    teams[winner][POINTS] += 3

def draw(teams, team):
    teams[team][TIES] += 1
    teams[team][POINTS] += 1

def played(values):
    return values[1][WINS] + values[1][LOSSES] + values[1][TIES]

def read_team(teams):
    team1, goals1, goals2, team2 = input().replace("#", "@").split("@")

    # Processes the goals
    teams[team1][GOALS_FOR] += int(goals1)
    teams[team2][GOALS_AGAINST] += int(goals1)
    teams[team2][GOALS_FOR] += int(goals2)
    teams[team1][GOALS_AGAINST] += int(goals2)

    # Choses the winner:
    if goals1 > goals2:
        win(teams, team1, team2)
    elif goals2 > goals1:
        win(teams, team2, team1)
    else:
        draw(teams, team1)
        draw(teams, team2)


def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        tournament_name = input()
        team_count = int(input())
        teams = dict()

        for __ in range(team_count):
            teams[input()] = [0]*(LOSSES+1)

        matches = int(input())
        for __ in range(matches):
            read_team(teams)

        print(tournament_name)
        test = sorted(teams.items(), key=lambda t: (t[1][0], t[1][1],
                                                    t[1][2]-t[1][3],
                                                    t[1][2]), reverse=True)

        for idx, value in enumerate(test):
            print("%d) %s %dp, %dg (%d-%d-%d), %dgd (%d-%d)" %
                  (idx + 1, value[0], value[1][POINTS], played(value), value[1][WINS],
                   value[1][TIES], value[1][LOSSES], value[1][GOALS_FOR]
                   - value[1][GOALS_AGAINST], value[1][GOALS_FOR],
                   value[1][GOALS_AGAINST]))
        if test_case < test_cases-1: 
            print()

if __name__ == "__main__":
    main()
