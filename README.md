# Overview
This is a simple program using the sqlite3 library for Python. It references a database pulled from the SQLite tutorial site, chinook.db.

I wrote this to practice writing SQL queries and to get a feel of using 

Below is a link to a video demonstrating this program:

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

This program references the chinook database from the SQLite tutorial site, referenced below. It has tables for an music shop, including customers, 
employees, albums, artists, tracks, etc.

The tracks table has the most relations, relating to playlist_track, media_types, invoice_items, genres, and albums. Every table has an incremental ID,
with fields for expected charateristics, like track length, album name, etc.

# Development Environment

I used VSCode and Python 3.10 to develop this, and the sqlite3 library for SQL database interaction.

# Useful Websites

I referenced these sites in working on this project:

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [SQLite Official Site](https://docs.python.org/3.8/library/sqlite3.html)

# Future Work

- Add more lookup queries for the other tables.
- Add more options to find related data
- Add more error catching