from staticjinja import make_site

# browser-sync start --server --files "*"
if __name__ == '__main__':
    context = {'ids': [{'name': 'Андрей', 'date': 'вчера', 'time': '21:30',
                        'text': '60 шт. ПК от 72-15 до ПК 21-15, Криводановка, с доставкой.', 'views': '12 просмотров'
                        }]*4}
    site = make_site(contexts=[('index.html', context), ('leads.html', context)])
    site.render(use_reloader=True)


