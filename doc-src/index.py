import os, os.path, subprocess
import countershape.widgets
import countershape.layout
import countershape.grok
from countershape.doc import *

this.layout = countershape.layout.Layout("_layout.html")
this.markdown = "rst"

ns.docTitle = "Cubictemp Manual"
ns.docMaintainer = "Aldo Cortesi"
ns.docMaintainerEmail = "dev@nullcube.com"
ns.copyright = "Copyright Nullcube 2008"
ns.head = countershape.template.File(None, "_header.html")
ns.sidebar = countershape.widgets.SiblingPageIndex(
                '/index.html',
                exclude=['countershape']
            )

this.titlePrefix = "Cubictemp Manual - "

ns.ctgrok = countershape.grok.parse("../cubictemp.py")

pages = [
    Page("index.html", "Introduction"),
    Page("subs.html", "Tags"),
    Page("blocks.html", "Blocks"),
    Page("processors.html", "Processors"),
    Page("api.html", "API"),
    Page("admin.html", "Administrivia")
]
