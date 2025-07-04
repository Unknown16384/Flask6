from flask import Flask, request

app = Flask(__name__)
notes = []

@app.route('/')
def all_notes(): return notes
@app.route('/', methods=['POST'])
def add_note():
    note = request.get_json(force=True)
    notes.append(note)
    return note
@app.route('/<int:index>')
def get_note(index): return notes[index]
@app.route('/<int:index>', methods=['PUT'])
def put_note(index):
    note = request.get_json(force=True)
    notes[index] = note
    return notes[index]
@app.route('/<int:index>', methods=['DELETE'])
def del_note(index):
    del notes[index]
    return notes

if __name__ == '__main__':
    app.run(port=80, debug=True)