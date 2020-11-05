import fasttext
import sys
import json
import numpy as np
model_path = sys.argv[1]
string_list_path = sys.argv[2]
output_path = sys.argv[3]
with open(string_list_path) as f:
  strings = json.load(f)
model = fasttext.load_model(model_path)
out_vectors = []

for string in strings:
  out_vectors.append(model[string])
np.save(output_path, out_vectors)
