from flask import Flask, abort, render_template


app = Flask(__name__)


MDB = {
    123: {'name': 'Titanic', 'year': 1995},
    124: {'name': 'Smile', 'year': 1985}
}


@app.route('/')
def list_movies():
    # connect to database

    # get 10 recent movies

    # render html table with 10 movies

    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
    return ('<html>'
            '<body><b>Hello!</b></body>'
            '</html>')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/movies')
def movies():
    return render_template('movies.html', movies=MDB)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    movie = MDB.get(movie_id)

    if not movie:
        abort(404)

    return render_template('movie.html', movie=movie)


if __name__ == "__main__":
    app.run(debug=True)
