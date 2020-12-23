.. Langman documentation master file, created by
   sphinx-quickstart on Sun Dec 13 15:54:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Langman documentation
=====================

Flask Server API
________________

.. automodule:: server.app
   :members:

Database ORM and schema
_______________________

.. automodule:: server.langman_orm
   :members:

Client Stylesheet
_________________

`Storybook Stylesheet <_static/storybook-static/index.html>`_
(Requires JavaScript)

Client Application
__________________

The following describes  the JavaScript client.

.. js:module:: App

.. js:class:: App

    .. js:method:: constructor(props)

       The React lifecycle method to intialize the component. Sets
       the state ``gameStatus`` to 'logged out'. Also, binds methods.

       :param props object:  The collection of properties for the
                             object, which are typically set using JSX
                             within a render method, but for this top
                             level component come directly from React.

    .. js:method:: startGame(nameValue, langValue)

       Contacts server to start a new game, then updates state accordingly.

       :param nameValue string: name of player
       :param langValue string: Two-letter string indicating language choice

       State is set for ``username``, ``language``, ``gameId``,
       ``badGuesses``, ``guessed, ``playerId``, ``revealWord``,



Welcome to Langman's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
