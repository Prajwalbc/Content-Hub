from flask import Flask, render_template, jsonify
import pickle
import requests

app = Flask(__name__)

movie_list_pkl = pickle.load(open('./model/movie_list.pkl','rb'))
similarity = pickle.load(open('./model/similarity.pkl','rb'))

movieList =  movie_list_pkl['title'].values

# Templates
@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/recommend')
def recommend_page():
    return render_template("recommend.html")

@app.route('/movies')
def movies():
    return render_template("movies.html")

@app.route('/movies/<movie_id>')
def get_movie_desc(movie_id):
    return render_template("movie_desc.html")
    

# APIs

#Movies section
@app.route("/api/now_playing")
def now_playing():
    #now playing
    url = "https://api.themoviedb.org/3/movie/now_playing?api_key=981e4edeb003b823a185e465213bc596&language=en-US&page=1"
    now_playing = requests.get(url)
    return now_playing.json()

#Recommend section
@app.route('/api/movies')
def movies_api():
    return jsonify(movieList.tolist())

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=981e4edeb003b823a185e465213bc596&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

@app.route('/api/recommend/<movie>', methods=['GET'])
def recommend_api(movie):
    try:
        index = movie_list_pkl[movie_list_pkl['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []
        for i in distances[1:6]:
            # fetch the movie poster
            movie_id = movie_list_pkl.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movie_list_pkl.iloc[i[0]].title)

        return jsonify(recommended_movie_names, recommended_movie_posters)
    except:
        print("**********SERVER ERROR************")
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)