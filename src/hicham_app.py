from __main__ import app

@app.route('/hicham')
def hicham():
    return 'hicham Page'

@app.route('/hicham2')
def hicham2():
    return 'Second hicham Page'