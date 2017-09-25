#! /usr/bin/env python
from __future__ import absolute_import
import os, glob, shutil, string, pickle, gzip


from jinja2 import Environment, PackageLoader, select_autoescape




if __name__ == "__main__":
    import doctest
    doctest.testmod()



    env = Environment(
        loader=PackageLoader('python-tikz', 'templates'),
        autoescape=select_autoescape(['tex'])
    )


    template = env.get_template('graph_tikzpicture_template.tex')

    print template.render(nodeslist='pouet')
