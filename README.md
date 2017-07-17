# Coup
Fiction work.

## Usage

### How to clean it up for initial launch

1. Remove the first `<script>` tag and everything in it in `flask/application/templates/base.html`
2. Edit the Chapter 4 and remove the link to longpage. Replace it with a "visit tomorrow for the next installment of new chapters"
3. SSH into prod and delete the longpage directory. `ssh prod; cd /apps/fiction/coup; rm -fr longpage`
4. Also remove password protection (see instructions at the bottom of this file)
4. Edit `flask/application/thesite.py` and delete lines 43-56. This gets rid of the longpage code and makes sure we don't see it again.
5. Deploy! `cd flask; ./deploy.bash; ./deploy.bash --server prod`

### How to launch a new chapter

1. Edit `flask/application/__init__.py`
2. Add the chapters you want to launch to the second `app.chapters = ['01'...` list.
3. Add the date the chapters will launch to the particular chapter records in `flask/application/chapters.json`
3. Save and deploy

### How to edit page title tags

1. Open `flask/application/chapters.json`
2. Find the json item that corresponds with the page metadata you want to edit.
3. Edit, save, deploy.

### Social share implementation

The social share buttons are hard-coded. Large in-color links go below the `<h1>` in each chapter and on the homepage. You may have to crop and produce the graphics and add them to the repo yourself.

There's a new file in application/templates/includes/social.html -- the fb and twitter markup goes in there.

To add them to each page, use this template tag: `{% include 'includes/social.html' %}`

The facebook button should link to https://www.facebook.com/sharer.php?u=http://interactive.nydailynews.com/fiction/coup/

The twitter button should link to http://twitter.com/share?url=http://nydn.us/coup&text=The%20story%20of%20how%20Mike%20Pence,%20Rick%20Perry's%20dance%20leotard,%20and%20Ivanka%20save%20America%20from%20Donald%20Trump%20#thetrumpcoup



### How to bust cache when deploying new CSS

1. Edit `flask/application/templates/base.html`
2. Find the line with `site.css`
3. Append or edit the URL parameter on `site.css` so it looks something like `site.css?v2` (or v3, v4 etc.)

### How to turn off the password protection on prod

1. SSH in to prod
2. `cd /apps/fiction/coup/`
3. `rm .htaccess; rm .htpasswd`

## Technology

This is a [Flask](http://flask.pocoo.org/) app, which uses the [Jinja](http://jinja.pocoo.org/docs/2.9/templates/#) templating language.
