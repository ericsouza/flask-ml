import pathlib
import numpy as np
import pickle
from flask import request, jsonify

RFC_PKL_PATH = str(pathlib.Path().absolute()) + "/iris_rfc.pkl"

rfc = pickle.load(open(RFC_PKL_PATH, "rb"))


def iris_classication():
    data = request.get_json(force=True)
    x_args = np.array([[data["sl"], data["sw"], data["pl"], data["pw"]]])
    y_hat = rfc.predict(x_args)
    y_output = y_hat[0]
    return jsonify(result=int(y_output))
