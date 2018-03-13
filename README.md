Repo hosting the official documentation for [tagtog](https://www.tagtog.net). 

Take a look at [docs.tagtog.net](https://docs.tagtog.net/)

# Issues
Please report any issues here or contact us at <info@tagtog.net>
# Do you want to contribute?
## Getting started

### Clone the repo
```shell
git clone https://github.com/tagtog/tagtog-doc.git
cd tagtog-doc
```
### Run the documentation locally
1. Install [Ruby](https://www.ruby-lang.org/)
2. Install http://bundler.io/ `gem install bundle`
3. Install [Jekyll](https://jekyllrb.com/) `gem install jekyll`
4. `cd tagtog-doc`
5. Run jekyll locally `bundle exec jekyll serve`

## Style guide

### Layout
The documentation content is displayed in a two columns layout.
You are free to decide when to use these columns. But please always use both:

```html
<div class="two-third-column">
  Main content
</div>
<div class="one-third-column">
  Display messages, figures, etc.
</div>
```
### Right column messages

Use messages only on the right column of the layout `one-third-column`. Display tips, tricks and other interesting stuff.

Template `message.html`:
```html
{% include message.html message="your tips and tricks"%}
```

### Images

#### Regular images

Use it to display images. Optionally you can set the `width` and the `caption`.

Template `image.html`:

```html
{% include image.html name="editor-import.png" caption="Upload box where you can select how to import text" %}
```

#### Inline images
Use it to display an image within the text. You can optionally set the `width` to adjust the size of the image.

Template `inline-image.html`:

```html
{% include inline-image.html name="image-inline.png" width="70" %}
```

### Features not yet ready
To mention features that will be ready soon, use the CSS class `soon`. The content will be faded

```html
<div class="soon">
  Text streams coming soon
</div>
```



