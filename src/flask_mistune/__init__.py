from .markdown import render


class Mistune:
    def __init__(self, app=None, **params):
        self.params = params
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.jinja_env.filters.setdefault('markdown', self.render)

    def render(self, text):
        return render(text)


__all__ = [
    'Mistune',
]

__version__ = '0.5'
