from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'Home Page'

@app.route('/page/<int:page_id>')
def id_page(page_id):
    # if page_id == 1:
    #     return 'Page 2'
    return f'Page {page_id}'


@app.route('/page/<int:page_id>/<page_name>')
def id_page_name(page_id, page_name):
    return f'Page {page_id} - {page_name}'

import martinJ_app
import martinG_app
import harry_app
import anko_app
import cor_app
import frank_app
import franquin_app
import hicham_app
import jordi_app
import linda_app
import nanno_app
import nico_app
import rob_app
import ronald_app



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

