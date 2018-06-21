import uuid
import os, glob
from staticjinja import make_site


if __name__ == '__main__':
    context = {
        'leads': [{
                    'name': 'Андрей', 'date': 'вчера', 'time': '21:30',
                    'text': '60 шт. ПК от 72-15 до ПК 21-15, Криводановка, с доставкой.', 'views': '12 просмотров'
                    }]*4,
        'STATIC_URL': 'static.{}'.format(uuid.uuid4().hex[:8])
    }

    static = glob.glob(os.path.join(os.getcwd(), "static.*"))[0]
    os.rename(static, context['STATIC_URL'])

    site = make_site(contexts=[('index.html', context), ('leads.html', context)])
    site.render(use_reloader=True)


