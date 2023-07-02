import requests

r = requests.post(
    "http://10.184.23.197:8080/api/generate",
    data = {
        "code": """
            def add(a,b):
                return a+B
        """
    }
)

print(r.text)  # displays the result body.
