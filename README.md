# Comfortably Numb

Python Flask SQLite app

## Features included:

- 100px fixed header
- 200px wide left navigation
- Main content fills remaining width and height
- Sticky footer always visible at bottom
- Footer has centered copyright and right-aligned navigation labels
- Fully responsive flexbox layout
- Clean, modern look with subtle hover effects

### to run

```
python app.py
```

may need to all create the virtual environment (before running)

```
python -m venv venv
```

### pages (routes)

1. Home: static, does nothing
2. Blog: static, does nothing
3. Books: added table for display of defined books

- click + button to navigate to form to add book
- books saved in SQLite db file named _numb.db_

### notes

- routes, including home/blog/books pages, defined in app.py
- added Google Font for handwriting style on home page

### to do

- implement static folder for style, images, scripts
