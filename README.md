Repo containing the official documentation for [🍃tagtog](https://www.tagtog.net).

The latest stable documentation is hosted at [docs.tagtog.net](https://docs.tagtog.net/).


# Issues

Please report any issues here or contact us at [info@tagtog.net](mailto:info@tagtog.net)


# Do you want to contribute?

## Clone the repo

```shell
git clone https://github.com/tagtog/tagtog-doc.git
cd tagtog-doc

```

## Run the documentation locally

You need a **docker** installation. Then simply:

```shell
./dev.sh
```


## Add new pages

1. Create a markdown `.md` file and add the [frontmatter](https://jekyllrb.com/docs/frontmatter/).
    ```html
    ---
    layout: page
    title: Multi-user annotation
    sidebar_link: true
    id: collaboration
    ---
    ```
    Choose an `id` and a `title`. Change the flag `sidebar_link` appropriately if you want a link to appear in the sidebar.

2. If the item is to appear in the side bar, add it to the `_config.yml` var `sidebar_toc`.
3. Follow the style guide below.

## Style guide

Documentation theme is based on [https://fongandrew.github.io/hydeout/](https://fongandrew.github.io/hydeout/)

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

### Lists

#### Ordered lists

Combine CSS classes `numbered-item` and `number-x`, where `x` is the order in the list. Currently the style is limited to the first 6 items. You decide the values for the ordered list, it can be numbers (1,2,3 ...), letters (A, B, C ...), etc. You can choose the order (e.g. 3, 2, 1).

```html
<p class="numbered-item"><span class="number-1">1</span>Description 1.</p>
<p class="numbered-item"><span class="number-2">2</span>Description 2.</p>
<p class="numbered-item"><span class="number-3">3</span>Description 3.</p>
```

#### Unordered lists

Combine CSS classes `list-item` and `list-item-x`, where `x` is the order in the list. Currently the style is limited to the first 6 items.

```html
<p class="list-item"><span class="list-item-1"></span>Description.</p>
<p class="list-item"><span class="list-item-2"></span>Description.</p>
<p class="list-item"><span class="list-item-3"></span>Description.</p>
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

### tagtog features not yet ready

To mention tagtog features that will be ready soon or have been temporarily disabled, use the CSS class `soon`. The content will be faded

```html
<div class="soon">
  Text streams coming soon
</div>
```

### Mix Markdown and HTML

```html
<div markdown="1">
  Your markdown
</div>
```

### Emojis

Use https://gist.github.com/rxaviers/7360908 , e.g. `:bookmark_tabs:` :bookmark_tabs:
