from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/about')
def about() :
    return render_template("about.html")

@app.route('/projects')
def projects() :
    return render_template("projects.html")

@app.route('/experience')
def experience() :
    return render_template("experience.html")

@app.route('/contacts')
def contacts() :
    return render_template("contacts.html")

if __name__ == "__main__" :
    app.run(debug=True)
