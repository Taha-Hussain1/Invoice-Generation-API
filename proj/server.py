from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
app.config['CSVFiles'] = 'static/CSVFiles'

class CSVFile(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return 'Hello world!'

@app.route('/invoice/CSV', methods = ['GET', 'POST'])
def index():
    form = CSVFile()
    if (form.validate_on_submit()):
        file = form.file.data
        file.save(app.config['CSVFiles'] + file.filename)
    return render_template('index.html', form = form)

@app.route('/invoice/JSON')
def create_invoice_JSON():
    return "create invoice JSON"

@app.route('/clear/invoice/<int:id>')
def clear_invoice(id):
    return f"delete invoice {id}"

@app.route('/invoice/<int:id>', methods = ['GET', 'PUT'])
def get_invoice(id):
    if request.method == 'GET':
        return f"get invoice {id}"
    elif request.method == 'PUT':
        return f"update invoice {id}"

@app.route('/invoice')
def get_ids():
    return "list of invoice ids"

if __name__ == "__main__":
    app.run(debug=True)
