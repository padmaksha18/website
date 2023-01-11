from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='192.168.1.151')
  #We made two new changes