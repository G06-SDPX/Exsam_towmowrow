from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(num):
    if num <= 1:
        return "False"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "False"
    return "True"

@app.route('/is_prime/<int:number>', methods=['GET'])
def check_prime(number):
    result = is_prime(number)
    return result
if __name__ == '__main__':
    app.run(debug=True)