from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return f"hellow kya haal chal"
if __name__ == "__main__":
    app.run(debug = True)# ye manually chlti rhegi baaar baar run krne ki jarurat ni



