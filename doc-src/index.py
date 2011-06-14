import os, os.path, subprocess
import countershape
from countershape import widgets, layout, markup
from countershape.doc import *

this.markup = markup.Markdown(extras=["code-friendly"])

ns.docTitle = "Cubictemp Manual"
ns.docMaintainer = "Aldo Cortesi"
ns.docMaintainerEmail = "dev@nullcube.com"
ns.copyright = "Copyright Nullcube 2008"
ns.head = countershape.template.File(None, "_header.html")
ns.sidebar = countershape.widgets.SiblingPageIndex(
                '/index.html',
                exclude=['setup.py']
            )
this.titlePrefix = "Cubictemp Manual - "
this.layout = countershape.layout.Layout("_layout.html")

pages = [
    Page("index.md", "Overview"),
    Page("introduction.md", "Introduction"),    
    Page("templates.md", "Templates"),    
    Page("extensions.md", "Extensions"),    
    Page("tipstricks.md", "Tips & Tricks"),    
    
    Page("blocks.md", "Blocks"),
    Page("processors.md", "Processors"),
    PythonPage("../cubictemp.py", 
        title="Source"),
    Page("subs.md","Tags, Expressions"),
    Page("admin.md", "Administrivia")
]
