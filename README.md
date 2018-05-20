# Quantified-self-py

Visit the deployed app at https://amj133.github.io/quantified-self-fe/index.html.  The deployed site consists of a javascript front end connected to this python Django backend.  The backend consists of several API endpoints that are fetched from the JS frontend depending on user input.  This project was unique in that the front end application was provided to us, and we had to build the backend application first in rails, then in express with node.js, and finally in a language of our choice.  I choose python Django because of its prevalence in the GIS and scientific communities.  Although there was some initial adjustment to Django, I was impressed with how easy it was to adapt to a new framework after building most of my previous applications in Rails.  I plan on building on my python skills by exploring Flask, and specifically how Flask can combine with PostGIS to perform custom spatial queries on datasets.

See the deployed project here: [Quantified Self](https://amj133.github.io/quantified-self-fe/index.html)

See the Rails and Express versions of this project here: 

[Quantified Self Rails Backend](https://github.com/amj133/quantified-self)

[Quantified Self Express Backend](https://github.com/amj133/quantified_self_express)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

1. clone down this project, change into the directory, and install all packages with pip
```
git clone https://github.com/amj133/quantified-self-py
pip install -r requirements.txt
```
2. create and migrate the database
```
python manage.py makemigrations tracker
python manage.py migrate
```
3. Run python server and visit localhost:3000 in your browser
```
python manage.py runserver 3000
```
*visit http://localhost:3000 in your browser
*enjoy!

### Prerequisites

* pip
* Python 3+
* Django 1.11.13

## Running the tests

To run the tests, follow the instructions in [Getting Started](#getting-started) above first.  Open the project directory then run the code below.
```
python manage.py test
```

## Contributing

Feel free to make pull requests or comments to contribute to this application. I am happy to receive your feedback!

## Authors

* [Andrew Jeffery](https://github.com/amj133)

## Acknowledgments

* Thank you to our awesome instructors at Turing for help and guidance during this project!
