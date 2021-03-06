
Tags and Expressions
====================

Cubictemp evaluates expressions between tag delimiters as expressions in the
specified namespace. The result is converted to a string, and placed in the
rendered template. There are two flavours of delimiters - __escaped__:

<pre class="output">
<!--(block|cubescript)-->
@_!...!@
<!--(end)-->
</pre>

and **unescaped**:

<pre class="output">
<!--(block|cubescript)-->
$_!...!$
<!--(end)-->
</pre>

In Python, an <b>expression</b> can be thought of as anything that can be
assigned to a variable. Arithmetic operators, boolean operators, parentheses
for grouping, method/function calls, object instantiation and conditional
expressions are all valid components of expressions. Python <b>statements</b>
include things like <b>while</b>, <b>print</b>, variable assignment and full
<b>if</b> blocks.  Cubictemp allows <b>only expressions</b> in subtitution
tags. 


Example
-----------

Template:

<pre class="output">
<!--(block|cubescript)-->
@_!foo!@ times two is @_!foo*2!@
@_!foo!@ squared is @_!foo*foo!@
@_!"yes" if (1==2) else "no"!@
key is @_!mydict["key"]!@
<!--(end)-->
</pre>

Code:

<!--(block|syntax("py"))-->
import cubictemp
print cubictemp.File(
            "template",
            foo=3,
            mydict=dict(key="value")
        )
<!--(end)-->

Output:

<pre class="output">
3 times two is 6
3 squared is 9
no
key is value
</pre>


Escaping
========

In an escaped substitution tag, the &amp;, &lt;, &gt;, &quot;, &#146;
characters are converted to their corresponding HTML escape sequences.  Always
use the <b>escaped</b> substitution syntax if you can. When you really need to
place HTML in a substitution tag, make sure you carefully evaluate the
application context to make sure that users cannot inject malicious data.


Example
-----------

<!--(block|cubescript|syntax("py"))-->
import cubictemp
print cubictemp.Template(
        "@_!x!@ $_!x!$",
        x = "<H1>foo</H1>"
    )
<!--(end)-->

... will print:

<!--(block|syntax("html"))-->
<H1>foo</H1> &lt;H1&gt;foo&lt;/H1&gt;
<!--(end)-->


Controlling Escaping
====================

Sometimes, it is handy to be able to construct objects that bypass Cubictemp's
escaping mechanism, regardless of the type of tag in which they occur. You can
signal this to cubictemp by giving the object a special attribute
<b>_cubictemp_unescaped</b> which evaluates to true.

__Template__, __File__, and named block objects all have a
<b>_cubictemp_unescaped</b> attribute, so none of these objects will be escaped
when referenced inside an escaped tag.

