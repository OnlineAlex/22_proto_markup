import uuid
from staticjinja import make_site


if __name__ == '__main__':
    context = {
        'leads': [{
                    'name': 'Андрей', 'date': 'вчера', 'time': '21:30',
                    'text': '60 шт. ПК от 72-15 до ПК 21-15, Криводановка, с доставкой.', 'views': '12 просмотров'
                    }]*4,
        'hash': '.{}'.format(uuid.uuid4().hex[:8])  # del 'hash' if you use localhost
    }
    site = make_site(contexts=[('index.html', context), ('leads.html', context)])
    site.render(use_reloader=True)


