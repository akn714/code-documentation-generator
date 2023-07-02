from pychatgpt import Chat, Options

options = Options()

# Enable, Disable logs
options.log = True

# Track conversation
options.track = True

# Use a proxy
options.proxies = 'https://code-documentation-generator.adarshkumar35.repl.co'

# Create a Chat object
chat = Chat(email="email", password="password", options=options)


# importing flask framework
from flask import Flask, request

app = Flask(__name__)

# api endpoint
@app.route('/api/generate', methods=['POST'])
def docGen():
    code = request.form['code']
    print(code)
    res = chat.ask(f"please generate a documentation in markdown formate for the code {code}")
    return res

# running the server
app.run(host='0.0.0.0', port='8080', debug=True)
