This is a LaTeX assignment template.

It is intended to contain all the assignments
that students will work on the during their 
studies. 

First of all while on the master branch, edit 
the following fields in master_template.tex:

1. Institute Name and website if possible
2. Institute logo
3. Author
4. Email

The idea behind this project is that, is to make students 
use git in other to become familiar with it. 
The courses that the students will submit their 
assignments will be branches on the master branch. 
And the assignment number for each course will
also be a branch on the course branch. 

For example if the name of the course is python
and there are 2 assignments that will be given for 
this course, then we will do the following. 
While on the master branch, the user must create a 
new branch and check the branch out. This can be done 
as follows:

$ git branch -b python

You should now be on the python branch. Next we rename 
master_template.tex to username_python.tex using 
git mv as follows: 

$ git mv master_template.tex evans_python.tex

We commit after this with 

$ git commit -m "Renamed master_template.tex to evans_python.tex"

Now open evans_python.tex with your favorite text
editor and edit the Course name field. In this case,
we write Python Programming.

We commit after this with

$ git commit -am "Changed course name to Python Programming"

Next we create a branch for each of the 2 
assignments as follows. 

$ for i in python_assignment_1 python_assignment_2; do git branch $i; done

Next we checkout python_assignment_1 branch and 
rename evans_python.tex to evans_python_assignment_1.tex
by doing the following:

$ git checkout python_assignment_1
$ git mv evans_python.tex evans_python_assignment_1.tex
$ git commit -m "Renamed evans_python.tex to evans_python_assignment_1.tex"

Now open evans_python_assignment_1.tex with your 
favourite text editor and change Assignment Number 
to Assignment 1 then commit it. 

$ git commit -am "Changed Assignment Number to Assignment 1

Next we repeat the same process for the branch
python_assignment_2. 

If you want to add a new brach for a new course, first 
checkout the master branch as follows: 

$ git checkout master

and repeat the process described using python above.
