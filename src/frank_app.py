from __main__ import app
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


@app.route('/frank')
def frank():
    return 'frank Page at',current_time