from flask import Flask
app =Flask(__name__)
@app.route("/")
def home():
  return "welcome to our application of weather detection current city")
app.run()


