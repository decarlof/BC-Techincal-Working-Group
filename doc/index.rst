==========================
BC Technical Working Group
==========================


.. image:: source/img/project-logo.png
   :width: 320px
   :alt: project


This `GitHub repository <https://github.com/decarlof/project>`_ 
provides a template to add `sphinx <http://www.sphinx-doc.org>`_ 
/ `Read The Docs <http://read-the-docs.readthedocs.io>`_
documentation to generate this
`Web Doc pages <https://bctwg.readthedocs.io>`_. 

These pages are written using `reStructuredText <http://www.sphinx-doc.org/en/stable/rest.html>`_
that allows *emphasis*, **strong**, ``literal`` and many more styles.

You can add a reference :cite:`rivers2017areadetector`, include equations like:

.. math::  V(x) = \left(\frac{1-\eta}{\sigma\sqrt{2\pi}}\right) \cdot exp\left({\frac{x^2}{2\sigma^2}}\right) + \eta \cdot \frac{\sigma}{2\pi} \cdot \frac{1}{x^2 + \left(\frac{\sigma}{2}\right)^2}

or 

.. math::  I_{white} = \int_{E_{1}}^{E_{2}} I(\theta,E) \cdot F(E)\,dE.

and tables:


+---------------+----------------+-----------------------------+
|    Member     |      Type      |        Example              |
+===============+================+=============================+
|     first     |    ordinal     |           1st               |
+---------------+----------------+-----------------------------+
|     second    |    ordinal     |           2nd               | 
+---------------+----------------+-----------------------------+
|     third     |    ordinal     |           3rd               |
+---------------+----------------+-----------------------------+

More examples:

.. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

.. warning:: Warning text.

.. note:: Note text.
    
.. image:: source/img/plot_profile_animation.gif


Content
-------

.. toctree::
   :maxdepth: 1

   source/about
   source/howtos
   source/meetings
   source/examples
   source/credits
