
# Book Tracking (SERVER)

This is the server side of a CRUD project used to register and track books that I am reading.



# Demo

![alt text](https://github.com/jmrfG/bookshelf-client/blob/main/demo.jpg?raw=true)



# How to Run

Prior to running the server side, there are a couple of things you should do. 

First, you should install all the dependencies by running:

``
    pip install -r requirements.txt
``


Then, inside \api folder, create a file named config.py and set the following constants:

``
    HOST = <server host>;
    DATABASE = <db name>;
    USER = <user>;
    UPASS = <pwd>
``

Finally, run the main.py file:

Note that, since the application works uppon a TCP/IP stack, it'll only function 100% correctly if the server side is already running.

## External dependencies

 - [Bookshelf client side](https://github.com/jmrfG/bookshelf-client)
 - [Node.js](https://nodejs.org/en/)
 - [React JS](https://reactjs.org)
 - [PostgreSQL](https://www.postgresql.org)
