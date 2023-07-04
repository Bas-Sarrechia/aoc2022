def score_rock_paper_scissor(player, opponent):
    score_factory = {
        'rock': {
            'paper': 0,
            'scissor': 6
        },
        'paper': {
            'scissor': 0,
            'rock': 6
        },
        'scissor': {
            'rock': 0,
            'paper': 6
        }
    }
    choice_score_factory = {
        'rock': 1,
        'paper': 2,
        'scissor': 3
    }
    return score_factory.get(player).get(opponent, 3) + choice_score_factory.get(player)


with open('day2.data', 'r') as file:
    data = file.read()
    translate_map_pt1 = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissor',
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissor'
    }
    translate_map_pt2 = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissor',
        'Y': {
            'rock': 'rock',
            'paper': 'paper',
            'scissor': 'scissor'
        },
        'Z': {
            'rock': 'paper',
            'paper': 'scissor',
            'scissor': 'rock'
        },
        'X': {
            'rock': 'scissor',
            'paper': 'rock',
            'scissor': 'paper'
        }
    }
    rps = list(map(lambda a: a.split(' '), data.split('\n')))
    rps_score_pt1 = list(
        map(lambda a: score_rock_paper_scissor(translate_map_pt1.get(a[1]), translate_map_pt1.get(a[0])), rps)
    )
    rps_score_pt2 = list(
        map(lambda a:
            score_rock_paper_scissor(translate_map_pt2.get(a[1]).get(translate_map_pt2.get(a[0])),
                                     translate_map_pt2.get(a[0])), rps)
    )
    print(sum(rps_score_pt1))
    print(sum(rps_score_pt2))
