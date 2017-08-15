# Code for the log analysis CLI app

import psycopg2
DBNAME = "news"

# connect to the database
db = psycopg2.connect(database=DBNAME)
c = db.cursor()


def most_popular_articles():
    '''Display the 3 most popular articles of all time'''
    query = ("select title, count(path) as views from articles join log on "
             "articles.slug = substring(path from 10) group by title order by "
             "views desc limit 3;")
    c.execute(query)
    popular_articles = c.fetchall()
    print "\nThe most popular articles of all time are: \n"
    # loop through tuple, add to the print statement and
    # convert tuple to string
    for row in popular_articles:
        print "{0} - {1} views".format(*row)
    print "\n\n"


def most_popular_authors():
    '''Display the most popular authors of all time'''
    query = ("select name, count(path) as views from authors inner join "
             "articles on authors.id = articles.author left join log on "
             "articles.slug = substring(path from 10) group by name "
             "order by views desc;")
    c.execute(query)
    popular_authors = c.fetchall()
    print "\nThe most popular authors of all time are: \n"
    # loop through tuple, add to the print statement and
    # convert tuple to string
    for row in popular_authors:
        print "{0} - {1} views".format(*row)
    print "\n\n"


def error_request():
    '''Display the day on which more than 1% of requests led to errors'''
    query = ("select time::date as day, cast(count(substring('404 NOT FOUND' "
             "from status)) * 100.0 / count(substring('200 OK' from status)) "
             "as decimal(10,1)) as error from log group by day having "
             "count(substring('404 NOT FOUND' from status)) * 100.0 / "
             "count(substring('200 OK' from status)) > 1;")
    c.execute(query)
    popular_authors = c.fetchall()
    print "\nThe day with request errors more than 1%: \n"
    # loop through tuple, add to the print statement and
    # convert tuple to string
    for row in popular_authors:
        print "{0} - {1}% errors\n".format(*row)

''' make calls to the function in order to query the news database
 present the results'''
most_popular_articles()
most_popular_authors()
error_request()

db.close()
