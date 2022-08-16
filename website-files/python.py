import sys
import json
import ast

data_to_pass_back = 'top_songs'


# list
# input = ast.literal_eval(sys.argv[1])
# output = input
# output.append(data_to_pass_back)
# print(json.dumps(output))

# dict
input = ast.literal_eval(sys.argv[1])
output = input
output['data_returned'] = data_to_pass_back
print(json.dumps(output))

sys.stdout.flush()