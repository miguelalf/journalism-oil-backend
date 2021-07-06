## Backend 'hidrocarburos de México'

This is a backend that is part of a project that pretends to display a correlation between differents fields took from 3 different public datasets served by the government.

It's important to use at the same time with the [Frontend](https://github.com/miguelalf/journalism-oil-frontend) and have installed python as well. This project was created with the following libraries:

- Python 3.9.1
- Django 3.2.3
- Pandas 1.2.4
- BeautifulSoup 4.9.3

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

### Author

- [@miguelalf](https://github.com/miguelalf)