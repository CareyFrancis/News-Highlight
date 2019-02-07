import urllib.request,json
from .models import News_Sources,News_Article
api_key=None
base_url=None
news_article_url=None
def configure_request(app):
    '''
    A function that takes in the application instance and replaces the value of variables set to none
    '''
    global api_key,base_url,news_article_url
    api_key=app.config['API_KEY']
    base_url=app.config['BASE_URL']
    news_article_url=app.config['NEWS_ARTICLE_URL']

def get_news_sources(category):
    '''
    A function that gets the json response to our url request
    '''
    get_news_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data=url.read()
        get_news_sources_response=json.loads(get_news_sources_data)
        news_sources_results=None
        # print(get_news_sources_response)
        if get_news_sources_response['sources']:
            news_sources_results_list=get_news_sources_response['sources']
            news_sources_results=process_sources_results(news_sources_results_list)
    return news_sources_results

def process_sources_results(news_sources_list):
    '''
    '''
    news_sources_results=[]
    for source in news_sources_list:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')
        category=source.get('category')
        url=source.get('url')

        news_object=News_Sources(id,name,description,category,url)
        news_sources_results.append(news_object)
    return news_sources_results

def get_news_articles(q):
    '''
    A function that returns a json response of news articles
    '''
    get_news_articles_url=news_article_url.format(q,api_key)
    with urllib.request.urlopen(get_news_articles_url) as url:
        data=url.read()
        data_response=json.loads(data)
        data_results=None
        if data_response['articles']:
            data_results = process_articles(data_response['articles'])
    return data_results

def process_articles(article_list):
    data_list=[]

    for article_data in article_list:
        id=article_data.get('id')
        title=article_data.get('title')
        author=article_data.get('author')
        url=article_data.get('url')
        urlToImage=article_data.get('urlToImage')
        description=article_data.get('description')
        publishedAt=article_data.get('publishedAt')

        if urlToImage:
            data_list.append(News_Article(title,author,url,urlToImage,description,publishedAt))

    return data_list