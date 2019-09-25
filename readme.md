Задание выполнено на ОС: Linux с использованием Python 3.7:

```bash
$ gtar xf lodkatest.tgz && cd $_   # or
$ git clone https://github.com/ol-eg/lodkatest.git && cd $_

$ pytnon3 -m venv venv-lodkatest
$ source venv-lodkatest/bin/activate
$ pip install -r requirements.txt
$ python manage.py test
$ python manage.py runserver
```

admin is enabled http://127.0.0.1/admin (user:admin, pass:admin)
there is little category structure in db file
API can be manually tested in a browser.
