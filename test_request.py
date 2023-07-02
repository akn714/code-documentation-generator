import requests

r = requests.post(
    "https://code-documentation-generator.adarshkumar35.repl.co/api/generate",
    data={'code': 
"""
def add(a, b):
	return a + b
"""
})

print(r.text)  # displays the result body.
