import json
import numpy as np
import joblib

questions = open('questions.json', 'r').read()
questions = json.loads(questions)
q_ids = list(questions['questions'].keys())


def predict_personality(data):
    init_arr = np.full((50), 3)
    indices = [q_ids.index(k) for k in data.keys()]
    init_arr[indices] = [x for x in data.values()]
    nis = (init_arr - 1) / 4
    model = joblib.load('personality_predict.joblib')

    ans = [round(1 - min(abs(cluster[indices] - nis[indices])) * 10, 4) for cluster in model.cluster_centers_]

    ans_obj = {
        "Extraversion": ans[0],
        "Neurotic": ans[1],
        "Agreeableness": ans[2],
        "Conscientiousness": ans[3],
        "Open to experience": ans[4],
    }

    return ans_obj
