spiffing.py
===========

Why hello there, kind sir! If you are the sort of web developer who feels a need for tea and crumpets whilst discussing the weather, this will be right up your alley. **spiffing.py** is a Python port of `Spiffing CSS <https://github.com/idiot/Spiffing>`_ (written by our friend `@idiot <https://twitter.com/idiot>`_), a CSS pre-processor for the gentlemanly web developer in all of us.

**spiffing.py** has one job, and one job alone: correcting the spelling errors prevalent in the language, created by our chums over in the States.

As of version ``1.1.0`` (and onwards), you can convert CSS back and forth between American and Proper English at your whim. Isn't it just lovely?

Requirements
------------

- Python 2.7.3

That's all!

To install:
-----------
Simply install the spiffing.py package, and use it directly in your applications to convert well written, classy CSS to CSS much more likely to be understood by our brethren in the States.

- ``pip install spiffing``
- ``import spiffing``
- Convert your wonderfully written, grammatically correct files to CSS (to help our non-English speaking friends use it).
- The class you'll want to use is ``spiffing.Monocle``.

A small example
---------------

.. code-block:: python
    
    import spiffing
    spiffing_css = """body {
        background-colour: grey !please;
        font-weight: plump;
        text-transform: capitalise;
    }"""
    stateside = spiffing.Monocle(spiffing_css)
    print stateside.american

And to spiff up your American English CSS:

.. code-block:: python

    import spiffing
    butchered_css = """body {
        background-color: gray !important;
        font-weight: bold;
        text-transform: capitalize;
    }"""
    proper = spiffing.Monocle(butchered_css)
    print proper.english
