# Database Documentation <!-- omit from toc -->

This document holds a overview of the database structure such as tables, columns, constraints, and any other relevant information related to the database.

## Table of Contents <!-- omit from toc -->
- [Tables](#tables)
  - [User](#user)
  - [Photos](#photos)
  - [Album](#album)
  - [AlbumImage](#albumimage)

## Tables

### User

This table stores user account information.

- `id`: Unique identifier for each user **Primary Key**
- `first_name`: User's first name
- `last_name`: User's last name
- `username`: User's username **Unique**
- `email`: User's email **Unique**
- `password`: User's hashed password
- `slug`: A url safe string

### Indexes <!-- omit from toc -->

Indexes belonging to the `user` table.

- username_idx: Index on the `username` field
- email_idx: Index on the `email` field 

----

### Photos

This table stores information about the uploaded images **Does not include images from albums**.

- `id`: Unique identifier for each image
- `image`: A string that points to the image url
- `name`: The name the user gave the image
- `status`: A string of either public or private
- `upload_date`: The date when the image was uploaded
- `user`: **Foreign Key** that references `user.id`

### Indexes <!-- omit from toc -->

Indexes belonging to the `photos` table.

- name_idx: Index on the `name` field
- user_idx: Index on the `user` field

----

### Album

This table stores information about albums.

- `id`: Unique identifier for each album **Primary Key**
- `name`: The name of the album (user named) **Unique**
- `status`: A string of either public or private
- `creation_date`: The date and time of when the album was created
- `user`: **Foreign Key** that references `user.id`

### Indexes <!-- omit from toc -->

Indexes belonging to the `album` table.

- album_name_idx: Index on the `name` field
- album_user_idx: Index on the `user` field

----

### AlbumImage

This table stores information about images that belong to a album.

- `id`: Unique identifier for each album image **Primary Key**
- `image`: A string that points to the image url
- `upload_date`: The date and time of when the album image was uploaded
- `album`: **Foreign Key** references `album.id`
- `user`: **Foreign Key** references `user.id`

### Indexes <!-- omit from toc -->

Indexes belonging to the `albumimage` table.

- `album_image_idx`: Index on the `image` field