from enum import Enum

import mistune
from flask import Markup

Plugin = Enum(
    'Plugin',
    [
        name.upper()
        for name in [
            'strikethrough',
            'footnotes',
            'table',
            'url',
            'task_lists',
            'def_list',
            'abbr',
        ]
    ],
)

default_plugins = [Plugin.STRIKETHROUGH, Plugin.FOOTNOTES, Plugin.TABLE]

mistune_markdown = mistune.create_markdown(
    escape=False,
    renderer='html',
    plugins=[plugin.name.lower() for plugin in default_plugins],
)


def render(text, **options):
    return Markup(mistune_markdown(text))
