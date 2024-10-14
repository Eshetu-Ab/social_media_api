# Social Media API

A RESTful API for a social media platform built using Django and Django REST Framework. This API supports various functionalities including user management, posts, comments, likes, reposts, hashtags, notifications, follows, feeds, and direct messaging.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Requirements](#requirements)
- [License](#license)

## Features

- **User Management**: Register, login, and manage user profiles.
- **Posts**: Create, read, update, and delete posts with media uploads.
- **Comments**: Comment on posts and view comments.
- **Likes**: Like and unlike posts.
- **Reposts**: Share posts with followers.
- **Hashtags**: Use and follow hashtags to categorize posts.
- **Notifications**: Get notified about likes, comments, and follows.
- **Follows**: Follow and unfollow other users.
- **Feed**: View a feed of posts from followed users.
- **Direct Messaging**: Send and receive private messages between users.

## Technologies

- **Backend**: Django (5.1.1)
- **REST Framework**: Django REST Framework (3.15.2)
- **Database**: SQLite (default, can be configured for PostgreSQL or MySQL)
- **Authentication**: JSON Web Tokens (JWT) using djangorestframework-simplejwt
- **Image Handling**: Pillow for image processing
- **Filter and Pagination**: django-filter for advanced querying and pagination support

## Installation

Usage
After starting the server, you can access the API at http://127.0.0.1:8000/api/.
Use tools like Postman or cURL to interact with the API.
API Endpoints
Authentication
Register: POST /api/users/signup/
Login: POST /api/users/login/
User Management
Get User Profile: GET /api/users/{id}/
Update User Profile: PUT /api/users/{id}/
Follow User: POST /api/follows/
Posts
Create Post: POST /api/posts/
Get All Posts: GET /api/posts/
Get Single Post: GET /api/posts/{id}/
Update Post: PUT /api/posts/{id}/
Delete Post: DELETE /api/posts/{id}/
Comments
Add Comment: POST /api/comments/
Get Comments for Post: GET /api/posts/{id}/comments/
Likes
Like Post: POST /api/likes/
Unlike Post: DELETE /api/likes/{id}/
Hashtags
Get Hashtags: GET /api/hashtags/
Notifications
Get Notifications: GET /api/notifications/
Direct Messaging
Send Message: POST /api/direct-messages/
Get Messages: GET /api/direct-messages/


Requirements
asgiref==3.8.1
Django==5.1.1
django-filter==24.3
djangorestframework==3.15.2
djangorestframework-simplejwt==5.3.1
pillow==10.4.0
PyJWT==2.9.0
sqlparse==0.5.1
tzdata==2024.2
