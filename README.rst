spiffing.py
===========

Why hello there, kind sir! If you are the sort of web developer who feels a need for tea and crumpets whilst discussing the weather, this will be right up your alley. **spiffing.py** is a Python port of `Spiffing CSS <https://github.com/idiot/Spiffing>`_ (written by our friend `@idiot <https://twitter.com/idiot>`_), a CSS pre-processor for the gentlemanly web developer in all of us.

**spiffing.py** has one job, and one job alone: correcting the spelling errors prevalent in the language, created by our chums over in the States.

Requirements
------------

- Python 2.7.3

That's all!

To install:
-----------
Simply install the spiffing.py package, and use it directly in your applications to convert well written, classy CSS to CSS much more likely to be understood by our brethren in the States.

- ``pip install spiffing``
- ``from spiffing import Spiffing``
- Convert your wonderfully written, grammatically correct files to CSS (to help our non-English speaking friends use it).

A small example
---------------

.. code-block:: python
    
    from spiffing import Spiffing
    spiffing_css = """body {
        background-colour: grey !please;
        font-weight: plump;
        text-transform: capitalise;
    }"""
    stateside = Spiffing(spiffing_css)
    print stateside.american
