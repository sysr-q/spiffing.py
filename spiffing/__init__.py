# -*- coding: utf-8 -*-
"""
spiffing.py allows one to write CSS in the Queen's English like such:
body {
    background-colour: grey !please;
    font-weight: plump;
    text-transform: capitalise;
}

and have it translated into the English our State-side friends use:
body {
    background-color: gray !important;
    font-weight: bold;
    text-transform: capitalize;
}
"""
from .spiffing import Spiffing