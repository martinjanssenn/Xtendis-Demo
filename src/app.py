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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')