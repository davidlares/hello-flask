from flask import Flask
# flask instance
app = Flask(__name__)

# first route
@app.route('/')
def hello_world():
    return "hello, world" # GET verb return

# script initialization
if __name__ == "__main__":
    app.run(host="0.0.0.0") # flask server run script
    # 0.0.0.0 is needed for remote access
