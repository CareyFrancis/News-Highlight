import os
class Config:
    '''
    This is ageneral configuration class
    '''
    BASE_URL='https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}&language=en'
    # api_key = os.environ.get('api_key')
    API_KEY='33e7c5156ffd4b12b95d0e000ed89c91'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG= True
    
config_options={
    'development':DevConfig,
    'production':ProdConfig
}