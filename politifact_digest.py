import sys
import json
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file) as f:
    file_contents = json.load(f)
output_list = [article['statement'] for article in file_contents]
with open(output_file, 'w+') as of:
    of.write(json.dumps(output_list))
