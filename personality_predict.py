import json
import math
import numpy as np
import joblib

model = joblib.load('personality_predict.joblib')
questions = open('questions.json', 'r').read()
questions = json.loads(questions)
q_ids = list(questions['questions'].keys())


answer_type = np.array([
    1, -1, 1, -1, 1, -1, 1, -1, 1, -1,
    1, -1, 1, -1, 1, 1, 1, 1, 1, 1,
    -1, 1, -1, 1, -1, 1, -1, 1, 1, 1,
    1, -1, 1, -1, 1, -1, 1, -1, 1, 1,
    1, -1, 1, -1, 1, -1, 1, -1, 1, 1
])


def predict_personality(data):
    init_arr = np.full((50), 3)
    indices = [q_ids.index(k) for k in data.keys()]
    init_arr[indices] = [x for x in data.values()]
    nis = (init_arr - 1) / 4


    cluster = model.predict([nis])

    ans_vals = (init_arr[indices]-3)*answer_type[indices]

    ans = []

    for i in range(5):
        ind = i * 2
        ans.append(round(((sum(ans_vals[ind:ind + 2]) + 4) / 8) * 100, 1))

    ans_obj = {
        "Extraversion": ans[0],
        "Neurotic": ans[1],
        "Agreeableness": ans[2],
        "Conscientiousness": ans[3],
        "Open to experience": ans[4],
        "cluster": cluster
    }

    return ans_obj
