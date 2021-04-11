"""Run all pytests for application."""
import pytest
from flask import Flask, Markup, render_template_string

from flask_mistune import Mistune, markdown


@pytest.fixture()
def client():
    """Configure Flask App.

    Flask app is a dummy application to test filters for this module.
    """
    app = Flask(__name__)
    app.config['TESTING'] = True
    Mistune(app)

    @app.route('/test')
    def markdown_template_filter():
        text = '~~testing markdown filter~~ *test*'
        return render_template_string('{{ text|markdown }}', text=text)

    @app.route('/test2')
    def markdown_template_block():
        test = '*test*'
        text = '{% filter markdown %}{{ test }}{% endfilter %}'
        return render_template_string(text, test=test)

    with app.test_client() as client:
        yield client


def test_render_template_filter(client):
    """Test template filtering."""
    resp = client.get('/test')
    assert resp.data.decode('utf-8') == ('<p><del>testing markdown filter</del> '
                                         '<em>test</em></p>\n')


def test_render_template_block(client):
    """Test template block."""
    resp = client.get('/test2')
    print(resp.data)
    assert resp.data.decode('utf-8') == u'<p><em>test</em></p>\n'


def test_markdown_function(client):
    """Test markdown rendering from a string."""
    string = 'this is a *markdown* string'
    assert markdown.render(string) == Markup('<p>this is a <em>markdown</em> string</p>\n')
