from flask import Flask, request, jsonify
import json
# Flask api for generating prime numbers using normal method and prime sieve, For input use postman app to check for this api and provide json data as input?

app = Flask(__name__)
@app.route('/prime', methods=['POST'])
def prime():

    data = request.get_json()
    n = data['n']
    prime_list = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return jsonify(prime_list)
