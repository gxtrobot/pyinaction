def getsum(score_list):
    total = 0
    for score in score_list:
        total = total + score
    return total

def print_list(score_list):
    for score in score_list:
        print('score:', score)

def getavg(score_list):
    total = 0
    for score in score_list:
        total = total + score
    avg = total/len(score_list)
    return avg

def getrate(score):
    rate = ''
    if score >= 90:
        rate = 'A'
    elif score >= 75:
        rate = 'B'
    elif score >= 60:
        rate = 'C'
    else:
        rate = 'D'
    return rate