from flask import Flask, render_template, request
from alignment import needleman_wunsch

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/align', methods=['POST'])
def align():
    seq1 = request.form['seq1']
    seq2 = request.form['seq2']
    alignment = needleman_wunsch(seq1, seq2)
    return render_template('result.html', alignment=alignment)

if __name__ == '__main__':
    app.run(debug=True)
