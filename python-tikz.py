#! /usr/bin/env python

import os, glob, shutil, string, pickle, gzip


from jinja2 import Environment, PackageLoader, select_autoescape




if __name__ == "__main__":
    import doctest
    doctest.testmod()



    env = Environment(
        loader=PackageLoader('yourapplication', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )


    template = env.get_template('mytemplate.html')

    print template.render(the='variables', go='here')
