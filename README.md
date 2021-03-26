# Instagram profile data capture

This project offers a REST API to extract and store data from a public [instagram](https://www.instagram.com) profile. In particular, the following information is obtained:

- Id
- Name
- Number of followers
- Number of followed
- Posts:
    - Post Id
    - Date
    - Caption
    - Media (as BLOB data)
    - Number of likes
    - Number of comments
    - Number of views (None in the image case)

For the extraction is used the library [instaloader](https://instaloader.github.io/as-module.html), and for storage the database engine [SQLite](https://www.sqlite.org/index.html).

Built on [Django 3.1.7](https://docs.djangoproject.com/en/3.1/).

## Local environment

### Prerequisites

- Python 3

## Local execution

1. Download or clone the repository.

2. Install dependencies:

    ```pip install -r requirements.txt```

3. Fire up the server:

    ```python manage.py runserver```



### Use of services

Using a platform to simulate an API Client (such as [Postman](https://www.postman.com/)) execute the following query:

```POST: http://localhost:8000/insert_instagram_profiles/```

Including a request like:

```
{
    "user_login" : "Patricio"
    "password_login" : "pass123"
    "user_names" : ["lewyfinnegan, "thenotoriousmma", "magnus_carlsen"]
}
```

Note that an instagram account is also requested for the log in [^1].

[^1]: I have been trying to generate a service that does not require credentials. The only viable way, as far as I know, is by rotating proxies to avoid blocking by instagram. I found a simple way to do it through an [API for Web Scraping](https://webscraping.ai/), however before finishing the implementation I reached the limit of free access in webscraping.ia. I hope to finalize it when I can continue using the tool (04/04/2021).

### Run test

Unit tests mocking requests to instagram data (and login):

```python manage.py test```   