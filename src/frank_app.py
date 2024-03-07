from __main__ import app

@app.route('/frank')
def frank():
    return 'frank Page'