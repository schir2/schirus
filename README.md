#schir.us _website_

## Setup

1. activate virtual environment
2. run `pip install -r requirements.txt`
3. create `/schirus/.env'` and add `SECRET_KEY=your_key` variable to the file.

## Migrations
Run the following manage shell commands in order 
`python manage.py shell` (To activate shell)
```
makemigrations
sqlmigrate users 0001
migrate
makemigrations blog
sqlmigrate blog 0001
migrate
```

## Features
- [ ] Blog
    - [ ] Models
        - [ ] Posts
            - [ ] Snippet Generator Method
            - [ ] Graphic Generator Method
            - [ ] Liked by current user Method
            - [ ] Like method
    - [ ] Views
        - [x] CategoryAutoCompleteView
        - [x] PostListView
        - [x] PostDetailView
        - [x] PostCreateView
        - [x] PostDeleteView
        - [x] PostUpdateView
        - [ ] PostSearchView
    - [ ] Templates
        - [ ] Base
        - [ ] List
        - [ ] Detail
        - [ ] Delete Popover
        - [ ] Create
        - [ ] Update
        - [ ] Search
    - [ ] Components
        - [ ] Like Button
    - [ ] Stylesheets
        - [x] Setup scc
        - [x] Convert css to scss
        - [ ] Figure out scss structure
        - [ ] colors.scss
            - [ ] select color palette
        - [ ] components.scss
            - [ ] .grid
            - [ ] .snippet
            - [ ] .button
            - [ ] .badge
        - [ ] fonts.scss
            - [x] primary font
            - [ ] secondary font
        - [x] lengths.scss
    - [ ] Javascript
        - [ ] Like Ajax Method