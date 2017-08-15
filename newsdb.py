# Code for the log analysis CLI app

import psycopg2
DBNAME = "news"

# connect to the database
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

def most_popular_articles():
    '''Connects to the database and display the 3 most popular articles of all time'''
    query = "select title, count(path) as views from articles join log on articles.slug = substring(path from 10) group by title order by views desc limit 3;"
    c.execute(query)
    popular_articles = c.fetchall()
    print popular_articles
    db.close()

most_popular_articles()

'''
Testing queries
gives all the path without the beginning /article/ 
SELECT substring(path from '.................$') from log limit 5;
SELECT substring(path from 10) from log limit 5;

Question 1 - What are the most popular three articles of all time?
select title, count(path) as views from articles join log on articles.slug = substring(path from 10)
group by title order by views desc limit 3;

Question 2 - Who are the most popular article authors of all time?
select name, count(path) as views from authors inner join articles on authors.id = articles.author 
left join log on articles.slug = substring(path from 10) group by name order by views desc limit 1;

Question 3 - On which day did more than 1% of requests lead to errors

starters - displays all status per day - select time::date as day, count(status) from log group by day limit 10;
starters - displays 200 or 404 per each day - select time::date as day, count(substring('404 NOT FOUND' from status)) from log group by day limit 10;

works on all. left with limiting it to only when the request errors was 1%
select time::date as day, count(substring('404 NOT FOUND' from status)) * 100.0 / count(substring('200 OK' from status)) as error from log group by day limit 15;
select time::date as day, count(substring('404 NOT FOUND' from status)) * 100.00 / count(substring('200 OK' from status)) as error > 1 from log group by day limit 20;

works but needs refactoring
select time::date as day, count(substring('404 NOT FOUND' from status)) * 100.00 / count(substring('200 OK' from status)) as error from log group by day having count(substring('404 NOT FOUND' from status)) * 100.00 / count(substring('200 OK' from status)) > 1;
refactored code
select time::date as day error from log group by day having count(substring('404 NOT FOUND' from status)) * 100.00 / count(substring('200 OK' from status)) > 1;
'''