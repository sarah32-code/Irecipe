from flask import Flask
from test3 import app






if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True)
    app.run(host="127.0.0.1", port=5001, debug=True)