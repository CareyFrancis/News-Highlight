class News_Sources:

    """
    clas to define the objects in the News_Sources class
    """

    def __init__(self,id,name,description,category,url):


        self.id=id
        self.name=name
        self.description=description
        self.category=category
        self.url=url


class News_Article:

    """
    class to define the objects in the News_Article class
    """

    def __init__(self,title,author,url,urlToImage,description,publishedAt):
        self.id=id
        self.title=title
        self.author=author
        self.url=url
        self.urlToImage=urlToImage
        self.description=description
        self.publishedAt=publishedAt