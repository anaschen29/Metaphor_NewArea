# app.py
from flask import Flask, render_template, request
from my_methods import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    classic_papers = []
    trending_papers = []
    summaries = []
    terminology = []
    books = []
    query = None


    if request.method == 'POST':
        query = request.form.get('query')


        classic_papers = find_classic_papers(query)
        trending_papers = find_trending_papers(query)
        summaries = find_summaries(query)
        terminology = find_terminology(query)
        books = find_books(query)

        

    return render_template('index.html', classic_papers=classic_papers, trending_papers=trending_papers, summaries=summaries, terminology=terminology, books=books, query=query)

if __name__ == '__main__':
    app.run(debug=True)
