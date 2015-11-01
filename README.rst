PyNetViz(Python Network Visualization)
========

A python network(graph) visualization with networkx

It works in IPython(Jupyter) 


Installing
----------

.. code-block:: python

    pip install pynetviz

Usage
-----

.. code-block:: python

    import networkx as nx
    import pynetviz.sigmajs as nvs

    G = nx.Graph()
    G.add_edges_from([(1,2),(2,3),(3,4),(5,6)])
    G.add_edge(1, 3)
    G.add_edge(1, 6)
    nvs.make_gexf(G)
    nvs.make_html(drawEdges='true')
    nvs.view_html()

Output:

.. image:: http://i.imgur.com/i5fQyuJ.png
  :alt: Network(Graph) Visualization


Layout
--------------------------

.. code-block:: python

    G = nx.Graph()
    G.add_edges_from([(1,2),(2,3),(3,4),(5,6)])
    G.add_edge(1, 3)
    G.add_edge(1, 6)
    layout = nx.spring_layout(G)
    nvs.make_gexf(G, layout)
    nvs.make_html(drawEdges='true')
    nvs.view_html()


Example
--------------------------

.. code-block:: python

    G = nx.karate_club_graph()
    layout = nx.spring_layout(G)
    nvs.make_gexf(G, layout, size=nx.degree_centrality(G))
    nvs.make_html(drawEdges='true')
    nvs.view_html(height=1000)


* ``G`` Graph object of networkx.
* ``layout`` Position nodes.
* ``size`` Size nodes.
* ``drawEdges`` True or False.
* ``height`` Window height size.
