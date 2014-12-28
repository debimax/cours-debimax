

```python
# ma feuille de style pour nbviewer
from IPython import utils
from IPython.core.display import HTML
import os
def css_styling():
    """Load default custom.css file from ipython profile"""
    base = utils.path.get_ipython_dir()
    styles = "<style>\n%s\n</style>" % (open('./custom.css','r').read())
    return HTML(styles)
css_styling()
```




<style>
/*
Placeholder for custom user CSS

mainly to be overridden in profile/static/custom/custom.css

This will always be an empty file in IPython
*/


/*@import url('http://fonts.googleapis.com/css?family=Crimson+Text');
@import url('http://fonts.googleapis.com/css?family=Kameron');
@import url('http://fonts.googleapis.com/css?family=Lato:200');
@import url('http://fonts.googleapis.com/css?family=Lato:300');
@import url('http://fonts.googleapis.com/css?family=Lato:400');
@import url('http://fonts.googleapis.com/css?family=Source+Code+Pro');
*/

/* Change code font 
.CodeMirror pre {
    font-family: 'Source Code Pro', Consolas, monocco, monospace;
}*/


div.text_cell_render {
    /*font-family: "Crimson Text";*/
    font-size: 12pt;
    line-height: 145%; /* added for some line spacing of text. */
}

div.text_cell_render h1,
div.text_cell_render h2,
div.text_cell_render h3,
div.text_cell_render h4,
div.text_cell_render h5,
div.text_cell_render h6 {
    /*font-family: 'Kameron';*/
    font-weight: 300;
}

div.text_cell_render h1 {
    font-size: 24pt;
}

div.text_cell_render h2 {
    font-size: 18pt;
}

div.text_cell_render h3 {
    font-size: 14pt;
}

.rendered_html pre,
.rendered_html code {
    font-size: medium;
    background: #f5f5f5;
}


.rendered_html blockquote {
    margin: 1em 2em;
    background: red;
}

.rendered_html ol {
    list-style:decimal;
    margin: 1em 2em;
}



</style>



%load_ext rmagic


```python

```
