# -*- coding: utf8 -*-
import random
from string import Template
from IPython.display import display, HTML
import networkx as nx

'''
    PyNetViz(Python Network Vizualization for linkurious) as nvl

    File name: linkurious.py
    Author: Kyunghoon Kim
    Date created: 10/14/2015
    Date last modified: 10/14/2015
    Python Version: 2.7
'''
__author__ = "Kyunghoon Kim"
__version__ = "0.1.0"
__email__ = "kyunghoon@unist.ac.kr"

def node_info(G, node_name, alpha=0.6, r=0, g=0, b=204, x=0, y=0, size=1):
    """Allocate a attribute of each node.
    
    Parameters
    ----------
    G: networkx.classes.graph.Graph
        Graph
    node_name: string or int
        Node Label
    alpha: float
        Transparent
    r: int
        Red of RGB
    g: int
        Green of RGB
    b: int
        Blue of RGB
    x: float
        position of x-axis
    y: float
        position of y-axis
    size: float
        size of node
    """
    if x == 0:
        x = random.random()
    if y == 0:
        y = random.random()
    G.node[node_name]['label'] = node_name
    G.node[node_name]['viz'] = {'color': {'a': alpha, 'r': r, 'g': g, 'b': b},
        'position': {'x': x, 'y': y, 'z': 0.0},
        'size': size}
    return G

def make_html(url='../src/iframe/pylinkurious.html', filename='./NetworkX_Graph.html'):
    html = """
<!DOCTYPE html>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>PyLinkurious</title>
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

  <iframe name="pylinkurious-iframe"
    src="$url?cb=setUpFrame"
    width="100%"
    height="500"
    frameborder="0"
    webkitallowfullscreen mozallowfullscreen allowfullscreen>
  </iframe>

  <script>
  // Function called once the iframe is initialized:
  function setUpFrame() {

    // Get Linkurious.js instance:
    var LK = window.frames['pylinkurious-iframe'].LK;

    // Update UI components
    LK.updateUI();

    // Load a graph sample:
    LK.sigma.graph.read({
      nodes: [
        { id: 'n0', label: 'Node 0', x: 0, y: 0, size: 1 },
        { id: 'n1', label: 'Node 1', x: 50, y: -10, size: 1 }
      ],
      edges: [
        {
          id: 'e0',
          label: 'Edge 0',
          source: 'n0',
          target: 'n1',
          size: 1
        }
      ]
    });

    // Display the graph:
    LK.sigma.refresh();
    LK.plugins.locate.center();

    console.log('nb nodes', LK.sigma.graph.nodes().length);
  }

  </script>
</body>
</html>
    """
    s = Template(html).safe_substitute(url=url)
    HTMLfile = open(filename, 'w')
    HTMLfile.write(s)
    HTMLfile.close()

def make_gexf(G, layout=None, size=None, filename='./NetworkX_Graph.gexf'):
    if layout and size:
        for node in G.nodes():
            G = node_info(G, node, size=size[node], x=layout[node][0], y=layout[node][1])
    elif layout and not size:
        for node in G.nodes():
            G = node_info(G, node, x=layout[node][0], y=layout[node][1])
    elif not layout and size:
        for node in G.nodes():
            G = node_info(G, node, size=size[node])
    else:
        for node in G.nodes():
            G = node_info(G, node)
    nx.write_gexf(G, filename)

def view_html(filename='./NetworkX_Graph.html', height=500):
    """Display the html file.
    
    Parameters
    ----------
    filename: string
        location of html file
    height: int
        height of iframe
    """
    html = """<iframe name="pylinkurious-iframe"
    src="$filename"
    width="100%"
    height="$height"
    frameborder="0"
    webkitallowfullscreen mozallowfullscreen allowfullscreen>
    </iframe>"""
    s = Template(html).safe_substitute(filename = filename, height = height)
    display(HTML(s))


