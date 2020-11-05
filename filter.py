import sys
import os
import json

input_folder = sys.argv[1]
output_file = sys.argv[2]
output_list = []
for file in os.listdir(input_folder):
    file_contents = open(input_folder+'/'+file).read()
    print(file)
    tweet_list = json.loads(file_contents)
    for tweet in tweet_list:
        try:
            if tweet['data']['lang'] == 'en':
                output_list.append(tweet['data']['text'])
        except:
            print(tweet)

with open(output_file, 'w+') as of:
    of.write(json.dumps(output_list))
