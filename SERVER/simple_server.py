from flask import Flask, request, jsonify

app = Flask(__name__)




if __name__ == '__main__':
    app.run()


@app.route('/sun')
def sun_function():
    return 'Sun is shining, but not always !'


@app.route('/beer')
def drink_beer():
    return 'Doh, beer'


@app.route('/nightcity', methods=['POST'])
def nightevents():
    global salary, name
    if request.method == 'POST':
        name = request.form.get('name')
        salary = int(request.form.get('money'))

    resp = {'Name': name + 'Silverhand',
            'Money': salary * 3
            }

    return jsonify(resp)
