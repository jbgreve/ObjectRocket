# ObjectRocket

To access the code, use any of the following methods:

To Clone (with HTTPS)
$ git clone https://github.com/jbgreve/ObjectRocket.git

To Clone (with SSH) 
$ git clone git@github.com:jbgreve/ObjectRocket.git

OR Download (via web browser) at:
https://github.com/jbgreve/ObjectRocket


The code can be run from a linux terminal by navigating to the "ObjectRocket" directory and typing the following commands:

docker build -t foo . && docker run -it foo

OR

sudo docker build -t foo . && sudo docker run -it foo

After various initialization text, the following prompt will appear:

Type '1' to run unit tests.
Type '2' to add items to the register/basket.
>>> 


"1" will run the unit tests. While "2" will allow the user to add items and see the current state of the register/basket.
