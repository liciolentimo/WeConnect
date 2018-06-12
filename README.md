[![Coverage Status](https://coveralls.io/repos/github/liciolentimo/WeConnect/badge.svg?branch=challenge2)](https://coveralls.io/github/liciolentimo/WeConnect?branch=challenge2)[![Build Status](https://travis-ci.org/liciolentimo/WeConnect.svg?branch=challenge2)](https://travis-ci.org/liciolentimo/WeConnect)

# WeConnect
WeConnect provides a platform that brings businesses and individuals together. This platform  creates awareness for businesses and gives the users the ability to write reviews about the  businesses they have interacted with.
### Prerequisites

* Python 3.6
____

### Installation

clone the repo:
```
$ git clone https://github.com/liciolentimo/WeConnect.git
```
and cd into the folder:
```
$ /WeConnect
```
create a virtual environment for the project.
```
$ virtualenv --python=python3.6 virtualenv-name
```
and activate virtual environment
```
$ source virtualenv-name/bin/activate
```
# Run
on your browser open up [http://127.0.0.1:5000/api/v1/](http://127.0.0.1:5000/api/v1/)
### Api Endpoints

| Endpoint | Functionality |
| -------- | ------------- |
| POST /api/v1/register | Creates a user account |
| POST /api/v1/login | Logs in a user |
| POST /api/v1/reset-password  | Password reset |
| POST /api/v1/businesses | Register a business |
| GET /api/v1/businesses  | Retrieves all businesses |
| PUT /api/v1/businesses/businessId | Updates a business profile |
| DELETE /api/v1/businesses/businessId | Remove a business |
| GET /api/v1/businesses/'businessId | Get a business |
| POST /api/v1/businesses/businessId/reviews | Add a review for a business |
| GET /api/v1/businesses/businessId/reviews | Get all reviews for a business |
