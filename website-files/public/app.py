import json
from flask import request
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/test', methods=['POST'])
def test():
  output = request.get_json()
  print(output)
  print(type(output))
  result = json.loads(output)
  print(result)
  print(type(result))
  return result

# print(test())

if __name__ == "__main__":
  app.run(debug=True)

# with open('Spotify_JSON/_js_in.json', 'w') as jsonfile:
#   json.dump(test(), jsonfile)