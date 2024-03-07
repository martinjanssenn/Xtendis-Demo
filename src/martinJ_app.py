from __main__ import app

@app.route('/martinJ')
def martinJ():
    return 'MartinJ Page test'

@app.route('/martinJ2')
def martinJ2():
    return 'MartinJ Page test 2'