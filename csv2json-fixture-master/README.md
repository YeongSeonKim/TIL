# csv2json-fixture
This script can be used to convert CSV data to [Django fixtures](https://docs.djangoproject.com/en/stable/howto/initial-data/) JSON format.

## Usage
```
python3 csv2json.py file.csv app.Model
python3 manage.py loaddata file.json
```

## License
This is Korean port of [maur1th's code](https://github.com/maur1th/csv2json-fixture) licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)

This is a Python 3 port of [Brian Gershon's code](https://djangosnippets.org/snippets/1680/) licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
