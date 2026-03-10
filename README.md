# json-api-docker-learn
*Task for learning (how to work with API, JSON and Docker?)*

## API
jsonplaceholder.typicode.com

## JSON categories
+ '/users': id, name, username, email, address (street, suite, city, zipcode, geolocation)
+ '/posts': userId, id, title, body
+ 'comments': postId, id, name, email, body (all includes of this section was commented bcs API doesn't answer correctly)

## Code work

Script gets data from API and get back statistics
+ Total count of users
+ Total count of posts
+ Total count of comments *(commented)*
+ Average count of comments per post *(commented)*
+ Count of posts without comments *(commented)*
+ Top-5 users by count of posts
+ Details about users (username, count of posts, count of comments on his posts) *(commented)*

Code get back exceptions:
+ KeyboardInterrupt
+ No data in categories
+ Timeout by 10 seconds
+ HTTP error

## Plans
+ Add new category from API ('/todos', '/photos', '/albums')
+ Find out how to fix work with '/comments'

## About Dockerfile
+ python v.3.10 slim with module "requests"
+ requests v.2.31.0
