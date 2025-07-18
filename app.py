from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample movie data
movies_by_genre = {
    "action": ["John Wick", "Mad Max: Fury Road", "Die Hard"],
    "comedy": ["The Mask", "Superbad", "The Hangover"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "sci-fi": ["Inception", "Interstellar", "The Matrix"]
}

@app.route('/picker', methods=['GET', 'POST'])
def picker():
    if request.method == 'POST':
        genre = request.form.get('genre')
        return redirect(url_for('movies', genre=genre))
    return render_template('picker.html', genres=movies_by_genre.keys())

@app.route('/movies/<genre>')
def movies(genre):
    genre = genre.lower()
    movie_list = movies_by_genre.get(genre, [])
    return render_template('movies.html', genre=genre, movies=movie_list)

if __name__ == '__main__':
    app.run(debug=True)
