Linear Algebra Toolkit Flask
============================

Flask webapp for linear algebra calculations.

Usage
-----

To get started, run the following in your terminal:

    $ python app.py

This will start a Flask development server for debugging on port 5000.

Technical Details
-----------------

The main page is a single-page application, which everything done through
Flask, Jinja, and Javascript. The contact form works through Javascript and
Google Forms, and the actual matrix action is performed through the Linear
Algebra Toolkit library that we wrote along with the MathJax Javascript library
to render the matrices nicely on the webpage.
