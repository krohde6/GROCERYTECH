Group 4
Read me

necessary software for running our project:
-homebrew
-mysql
-PyQt
-Basic sql server (terminal, mamp, intelliJ)

**** DO THESE IN ORDER ****

------- Homebrew installation Directions -------

1. in the command prompt/terminal, run the following command:

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


------- MySql Installation Directions/ -------

brew install mysql

------- PyQt Installation Directions -------
1. paste the following link into your browser and download the software package

 https://www.riverbankcomputing.com/software/pyqt/download5/

2. paste the following code into your command prompt/terminal:

pip3 install PyQt5


--------------------------------------------------------------------------------



------- How to run the project: -------



1. We will now be creating a clone folder with all of the necessary files. cd
into the directory that you would like the folder to be created. (For the sake
of simplicity, we used desktop).

2. In the command prompt, run the following command:

git clone https://github.com/krohde6/GROCERYTECH.git

    - to verify the success of this command, look into the directory that you
    placed the folder and check to see that there is a folder called "GROCERYTECH"
    populated with many files

2. To load the tables into mysql, cd into the "GROCERYTECH" folder and run the
following command in the terminal/command prompt:

mysql -u root GroceryTech < GroceryTech.sql

    - if this is successful, go to step 3 below. If this is unsuccessful, follow
    these next steps:
    run the following commands in the terminal:
        1. mysql -u root
        2. create database GroceryTech;
        3. exit;
        4. GroceryTech < GroceryTech.sql


3. finally while still in the GROCERYTECH directory, run the following command
in the terminal/command prompt:

python LoginRegister.py








