# Duwin
This is the Graph API for the Duwin e-library project for [Teacher Su Centre](https://www.teachersucenter.com). 
This is written using Django and graphene-django frameworks. 
The web, desktop and mobile clients, developed by my amazing tech team at 
[teachersucenter.com](https://www.teachersucenter.com), can be found [here](#frontend-clients).

## Frontend Clients
|         |                                                  |
|---------|--------------------------------------------------|
| website | https://github.com/teachersucenter/duwin_web     |
| desktop | https://github.com/teachersucenter/duwin-desktop |
| mobile  | https://github.com/teachersucenter/duwin_mobile  |


## Factory architecture?
I don't really know what a factory design pattern is.
But, reading [this](https://stackoverflow.com/questions/13744363/create-class-having-djangos-inner-meta-class-using-type-method) 
will help a lot while exploring the codes in [core/serializers]() 
and [core/schemas]().

I have taken an experimental (for me) approach in defining serializers and mutations
such that they are dynamically generated from models (actually, also for ObjectTypes as well,
but for documentary purposes, I defined them manually (maybe will fix later)).


### Motivation
The Duwin project is very simple. The scopes are defined well.
Thus, I wanted to take a different approach in the architecture.
The motivation behind the Duwin source code is to write as little 
code as possible. 


### Inheritance & Polymorphism
In order to achieve the goal of writing as little code as possible,
polymorphism and inheritance concepts were heavily used. Most classes
are defined using the <code>type()</code> function and dynamically generated
during runtime. This makes debugging from extremely difficult to 
downright impossible, and reading the code becomes a living hell for 
an unfamiliar programmer. 

### Django-inspired
In contrast to the above topic, since everything becomes dynamic, the codes are extremely short,
it's very easy to refactor and the logic still in a single place. 

A popular design pattern (more like a mindset) for Django
developers (https://www.dabapps.com/blog/django-models-and-encapsulation) called 
"Fat models, thin views" is a way of organising codes in such a way that
everything can be controlled in one place. The Duwin codebase is heavily 
inspired by this.

## References and other materials
These are some external sources that you could look into to gain more understanding about 
the Duwin project, about GraphQL and Django itself.

### Authentication
Setting up the JWT authentication that is compatible with both
REST and GraphQL APIs. 

https://asvrada.github.io/blog/django-graphql-jwt/
