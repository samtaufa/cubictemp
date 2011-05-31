import os, os.path, subprocess
import countershape
from countershape import widgets, layout, markup, PythonModule
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
    Page("index.mdtext", "Overview"),
    Page("introduction.mdtext", "Introduction"),    
    Page("templates.mdtext", "Templates"),    
    Page("extensions.mdtext", "Extensions"),    
    Page("tipstricks.mdtext", "Tips & Tricks"),    
    
    Page("blocks.mdtext", "Blocks"),
    Page("processors.mdtext", "Processors"),
    PythonPage("../cubictemp.py", 
        title="Source"),
    Page("subs.mdtext","Tags, Expressions"),
    Page("admin.mdtext", "Administrivia")
]
