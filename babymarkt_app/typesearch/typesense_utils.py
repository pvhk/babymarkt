import typesense
#from ..models import Ad, Picture
class TypeSearch:
    client = typesense.Client({
    'master_node': {
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http',
        'api_key': 'oj<o#d{oK5/>AS{'
    },
    'timeout_seconds': 2
    })

    @staticmethod
    def create_ads_collection():
        ADS_SCHEMA = {
            'name':'ads',
            'fields': [
                {'name':'title', 'type':'string'},
                {'name':'text', 'type':'string'},
                {'name':'price', 'type':'int32'},
                {'name':'bdd_od', 'type':'int32'},
                {'name':'is_active', 'type':'bool'},
                {'name':'category', 'type':'string'},
                {'name':'picture', 'type':'string'},
                {'name':'pub_date', 'type':'string'}
            ],
            'default_sorting_field': 'price'
        }
        return TypeSearch.client.collections.create(ADS_SCHEMA)
    @staticmethod
    def index_ad(bdd_id, title, text, price, is_active, category, picture, pub_date):
        new_ad = {
            'bdd_id':bdd_id,
            'title':title,
            'text':text,
            'price':price,
            'is_active':is_active,
            'category':category,
            'picture':picture,
            'pub_date':pub_date
        }
        return TypeSearch.client.collections["ads"].documents.create(new_ad)
    @staticmethod
    def search(content):
        query = {
            'q':content,
            'query_by':'title,text,category'
            }
        return TypeSearch.client.collections["ads"].documents.search(query)
    @staticmethod
    def delete_collection(collection_name):
        return TypeSearch.client.collections[collection_name].delete()
    @staticmethod
    def import_bdd():
        TypeSearch.create_ads_collection()
        ads = Ad.objects.all()
        for x in ads:
            pic = Picture.objects.filter(ad=x)[:1]
            x.pictures = pic
            if len(x.pictures) > 0:
                TypeSearch.index_ad(x.id, x.title, x.text, x.price, True, str(x.category), str(x.pictures[0].url), str(x.pub_date))
            else:
                TypeSearch.index_ad(x.id, x.title, x.text, x.price, True, str(x.category), "", str(x.pub_date))