# -*- coding: utf-8 -*-
import requests
from flask import Flask, render_template, request, redirect
from forms import GifSearchForm

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    search = GifSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('gifsearch.html', form=search)

@app.route('/results')
def search_results(search):
    search_string = search.data['search']
    if search.data['search'] == '':
        flash('Please enter your query into the search box!')
        return redirect('/')
    else:
        # display results
        results = requests.get(
        	'http://api.giphy.com/v1/gifs/search?q={keyword}&api_key=DLCVuTK6KZExOS7JoMq82bi5MaI6EbWO&limit=1'.format(keyword=search_string))
        gif_results = results.json()['data'][0]
        embed_url = gif_results['embed_url']
        print(embed_url)
        return render_template('results.html', result_url=embed_url)


if __name__ == '__main__':
	print("Starting webapp...")
	app.run(debug=True)

