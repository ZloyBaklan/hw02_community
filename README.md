# Yatube application (backend_community_homework)

Posts app created and registered.
The database is connected.
The ten most recent entries are displayed on the main page.
In the admin area, management of Post model objects is available: you can publish new posts or edit / delete existing ones.
The user can go to the page of any community, where the ten most recent posts from this group are displayed.

# Admin
Model Group is registered.
A custom admin panel has been created for the Post model:
The list of objects in the admin panel displays the fields pk, text, pub_date, author, group.
The content of the group field can be edited in the admin panel right in the list of Post objects.
Search by text field is available.
Filtering by the pub_date field is available.
If a field is not filled in, it displays the text -blank-.

# View functions
index (): Pass the ten latest Post model objects and content for the <title> tag to the posts / index.html template.
group_posts (): Passes the last ten Post model objects filtered by the group field to the posts / group_list.html template, and the content for the <title> tag.

#Addresses
For the Posts app, namespace = 'post' is set.
Name = 'index' is set for the main page.
A page with posts from a specific group is available at a URL like group / <slug> /.
For a page with group posts, name = 'group_list' is set.

# Templates
Template files are stored at the project level.
Templates are broken down into logical blocks and assembled using include and extend tags.
The statics are connected to the templates.
The templates match the design:
web_hw02_community_with_text.zip
In the index.html template, the link <a href=""> all posts in the group </a> directs the user to the page of the group that the post belongs to.
The main content of the page is passed from the view functions in the context dictionary.
The content of the <title> tag is different for different pages:
for the group page: Community entries <group_name>;
for the main page: Latest updates on the site.
