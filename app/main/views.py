from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_news_sources,get_news_articles
from ..models import News_Sources,News_Article
@main.route('/')
def index():
    '''
    A function that displays the main route page
    '''
    news_sources = get_news_sources('general')
    xxx = get_news_sources('sports')
    business = get_news_sources('business')

    return render_template('index.html',general=news_sources,sports=xxx,business=business)

@main.route('/articles')
def articles(id):
    '''
    A function that defines the article's objects
    '''
    source_articles=get_news_articles('id')

    return render_template('articles.html',articles=source_articles)

@main.route('/source')
def source():
	'''
	function returns index page and its data
	'''

	news_sources = get_source('sources')

	return render_template('newssource.html',sources = news_sources)

