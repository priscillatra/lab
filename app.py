from flask import Flask
import random

app = Flask(__name__)

secret = random.randint(1, 100)

@app.route('/guess/<int:num>')
def guess(num):
    if num < secret:
        return {"msg": "Higher"}
    elif num > secret:
        return {"msg": "Lower"}
    else:
        return {"msg": "Correct! 🎉"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
