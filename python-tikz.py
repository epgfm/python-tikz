#! /usr/bin/env python
from __future__ import absolute_import
import os, glob, shutil, string, pickle, gzip
import igraph as ig

from jinja2 import Environment, PackageLoader, select_autoescape


# Note: vertex_size attribute can be used.
# gameplan: use igraph for layout calculation then recover vertex size,


def gen_node(node, coords, i):
    template = env.get_template('node_template.tex')

    node["label"] = 'knoten' + str(i)
    node["name"] = 'knoten' + str(i)
    
    return template.render(x = coords[0]*10, y = coords[1]*10*-1, nodeid = node['name'], label=node['label'])

def generate_nodelist(g, layout):
    nodes = g.vs
    out = ""
    for i in range(len(nodes)):
        out += gen_node(nodes[i], layout[i], i)
    return out

def gen_edge(startnode, endnode, edgelabel):
    startnode = "knoten" + str(startnode)
    endnode = "knoten" + str(endnode)
    template = env.get_template('edge_template.tex')
    return template.render(startnode=startnode, endnode=endnode, edgelabel=edgelabel)


def generate_edgelist(g):
    edges = g.es
    out = ""
    for e in edges:
        if "weight" not in e.attribute_names():
            e["weight"] = ""
        out += gen_edge(e.source, e.target, e["weight"])
    return out


def gen_graph(g, layout=None):

    if layout == None:
        l = g.layout("kk")
    else:
        l = layout

    nodeslist = generate_nodelist(g, l)
    edgeslist = generate_edgelist(g)

    template = env.get_template('graph_tikzpicture_template.tex')
    return template.render(nodeslist=nodeslist, edgeslist=edgeslist)



def gen_standalonegraph(g, layout=None):
    template = env.get_template('standalone_tikzpic.tex')
    return template.render(tikzpic=gen_graph(g, layout=layout))




if __name__ == "__main__":
    import doctest
    doctest.testmod()



    env = Environment(
        loader=PackageLoader('python-tikz', 'templates'),
        autoescape=select_autoescape(['tex'])
    )


    template = env.get_template('graph_tikzpicture_template.tex')

    g = ig.Graph.GRG(20, 0.2)

    layout=g.layout('kk')
    ig.plot(g, layout=layout)

    print gen_standalonegraph(g, layout=layout)


