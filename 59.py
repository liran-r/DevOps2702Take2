import requests
response = requests.post("http://127.0.0.1:5001/whatismyname")
actual = "saved new car"
expected = response.text
print(response.text)
assert actual == response.text