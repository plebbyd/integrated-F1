#penalzed and non-penalized integrated F1 score calculator functions
#From GitHub by Plebbyd: https://github.com/plebbyd/integrated-F1

def penalized(conf, F1, f=1.0):
    pen_scores = [(conf[i+1] - conf[i]) * ((F1[i] + F1[i + 1]) / 2)**(f / ((conf[i] + conf[i+1]) / 2)) for i in range(0, len(conf) - 1)]
    overall_score = sum(pen_scores)
    pen_nonpen_ratio = overall_score / non_penalized(conf, F1)[1]
    return pen_scores, overall_score, pen_nonpen_ratio

def non_penalized(conf, F1):
    scores = [(conf[i+1] - conf[i]) * F1[i] for i in range(len(conf) - 1)]
    return scores, sum(scores)
