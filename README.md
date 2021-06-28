## Backend 'hidrocarburos de México'

It's important to use at the same time with the [Frontend](https://github.com/miguelalf/journalism-oil-frontend) and have installed python as well. This project was created with the following libraries:

- Django
- Pandas

### Installing steps

First install the requiriements in yor enviroment.

```
python3 -m pip install -r requirements.txt
```

After that run the following command, this create a csv file with the data required for the site

```
python3 getting_data.py
```

Start the service and have fun!

```
python3 backendPeriodismo/manage.py runserver
```