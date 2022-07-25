# ReminderMaker

## 事前準備
```
sqlite3.NotSupportedError: deterministic=True requires SQLite 3.8.3 or higher
```
このようなエラーが発生した場合、以下コマンドによってパッケージをインストールした後、プログラムを書き換える必要がある
```
pip install pysqlite3
pip install pysqlite3-binary
```
```python
# /.venv/lib/python3.9/site-packages/django/db/backends/sqlite3/base.py
# from sqlite3 import dbapi2 as Database # annotation
from pysqlite3 import dbapi2 as Database # import pysqlite3
```