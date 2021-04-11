# Flask-Mistune

Flask interface for mistune markdown parser

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/flamusdiu/flask-mistune/tests)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/flamusdiu/flask-mistune)
![GitHub all releases](https://img.shields.io/github/downloads/flamusdiu/flask-mistune/total?style=plastic)

## How to install

``` pip install flask-mistune ```

## How to use

```python
# import the packages
from flask_mistune import Mistune, markdown
```

```python
# register the app
Mistune(app)
```

```html

<!--use as a filter-->
<p>{{ text| markdown }}<p>

```
