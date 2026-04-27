# PythonJobsScrape
Scrapes the python jobs website for all of their current job listings and prints them to the screen

#Execution and Arguments#
Before getting started, make sure you have python installed as well as a few dependencies included. To install what is needed for this program enter this code seen below**

  python3 -m pip install bs4

To run this program and then navigate to the directory in which you stored it in (using cd followed by the path/directory) then type the following**:

  python3 python-jobs-scaper. py --keyword *keyword*

The keyword argument is optional, but allows you to filter the results for jobs that have that string in the title. Common keywords could be Senior, Research, or Developer. The keyword is not case sensitive. If you want to see the full list of jobs, then simply don't put any keyword at all.

**If you are using an older version of Python the *python3* command may be *python* instead.
