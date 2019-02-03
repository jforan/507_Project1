# Functionality

This app allows for a number of possibile outcomes.

* it welcomes users to the app
* welcomes it to a specific bank
* determines a value in a specific currency & displays the value in a more easily read-able format
* it then brings it all together to combine all those components into one output





# Requirements

* Flask
* lab3_code.py (this provides Currency, Yuan, Dollar, Pound, and Bank classes)

note: all requirements can be found acquired by running the requirements.txt file.




# How to Run

## Type in the command: python SI507_project1.py runserver

## Possible thing to type in the URL

note: you will change things in <>. it will begin with either http://127.0.0.1:5000/ or http://localhost:5000/, followed by the below options. typing in the URLs mentioned will bring users to the homepage.

* /bank/<name of bank>
* /dollar/<amt (number not written out)>
* /yuan/<amt (number not written out)>
* /pound/<amt (number not written out)>
* /bank/<name>/<currency>/<value (number not written out)>
