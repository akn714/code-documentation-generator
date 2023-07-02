from flask import Flask, request
from gpt4free import you

app = Flask(__name__)

def GPT_response(prompt, detailed=False, include_links=False):
    return you.Completion.create(
        prompt=prompt,
        detailed=detailed,
        include_links=include_links
    )

with open("query_prompt.txt", "r") as file:
    prompt = file.read()

# api endpoint
@app.route('/api/generate', methods=['POST'])
def docGen():
    code = request.form['code']
    query = prompt+code
    response = GPT_response(query).text;
    return response

# running the server
app.run(host='0.0.0.0', port='8080', debug=True)