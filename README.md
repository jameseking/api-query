# api-query
Performing a public API search query
What I performed:
I used the public API to perform searches in the Library of Congress newspaper data.  I wrote a program which prints the following data:
1.	Query for all newspaper publications and prints out the total number of newspapers.
2.	Query for all newspaper publications for which there is digital content and prints the state with the highest number of publications.  Prints the state name and the number of publications.
3.	Query for all newspaper publications for which there is digital content and prints the state with the least number of publications.  Prints the state name and the number of publications.
4.	Query for all newspaper publications for Alabama and prints out the state name and the total number of newspapers.
5.	Use the newspapers.json resource do the following for Oregon:
    1.	Prints out the state name and the total number of newspapers.
    2.	Loops through the newspapers and queries for additional information using the url property to do the following for the first 20 newspapers:
      1.	Prints the title of each newspaper
      2.	Prints the starting year of each newspaper
      3.	Prints the total number of issues available
