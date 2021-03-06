
Named blocks
=============

Cubictemp blocks are chunks of text that are defined in the template body, and
can be referenced in various ways.  The simplest block variety is the _named
block_:

<!--(block|cubescript|syntax("html"))-->
<!--(_block bar)-->
    The time has come the walrus said
<!--(_end)-->
one
@_!bar!@
two
@_!bar!@
three
<!--(end)-->

Output:

<pre class="output">
one
    The time has come the walrus said...
two
    The time has come the walrus said...
three
</pre>

Like a function, named blocks only produce output when they are referenced. The
block definition itself does not appear in the template output.

Named blocks are callable objects that accept an over-riding namespace
argument:

<!--(block|cubescript|syntax("html"))-->
<!--(_block bar)-->
    The time has come the @_!foo!@ said...
<!--(_end)-->
@_!bar(foo="walrus")!@

@_!bar(foo="carpenter")!@
<!--(end)-->

Output:

<pre class="output">
    The time has come the walrus said

    The time has come the carpenter said
</pre>

Blocks can be nested to arbitrary depths. Block namespaces and scopes work
similarly to Python namespaces and scopes.

Named blocks have the <b>_cubictemp_unescaped</b> attribute defined by default,
so they will go unescaped when inserted using the standard 
<!--(block|cubescript)-->
<code class="template">@_!...!@</code> 
<!--(end)-->
escaped substitution syntax.



<h1> Repeat Blocks </h1>

<p>Cubictemp provides a repeat construct to allow traversal of iterables:</p>

<!--(block|cubescript|syntax("html"))-->
<!--(_for foo in bar)-->
    @_!foo!@
<!--(_end)-->
<!--(end)-->

Like a Python __for__ loop, the template above loops through all elements of
"bar", setting the value of "foo" to each element in turn. As in simple
substitutions, any valid expression can be used as the sequence definition:

<!--(block|cubescript|syntax("html"))-->
<!--(_for foo in range(3))-->
    Counting: @_!foo!@
<!--(_end)-->
<!--(end)-->

Output:

<pre class="output">
Counting: 0
Counting: 1
Counting: 2
</pre>


Playing nice with your designers: closed and open tags
======================================================

There is a minor variation on the block definition syntax to help preserve
document structure during template design. Since the start and end directives
of Cubictemp blocks look like HTML comments, they are not visible when the
document is viewed as HTML. It is often convenient to be able to also comment
everything inside the block. This is accomplished using the __open__ tag
variation:

<!--(block|cubescript|syntax("html"))-->
<!--(_block foo)
    The time has come the walrus said...
(_end)-->
<!--(end)-->

<p> There is no functional difference between the two flavours.</p>

