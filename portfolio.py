from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(loader=PackageLoader('portfolio'),
                  autoescape=select_autoescape())

template = env.get_template('index.html')
print(template.render(name='Laura'))