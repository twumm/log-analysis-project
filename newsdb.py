#!/usr/bin/env python
# Code for the log analysis CLI app

import psycopg2
DBNAME = "news"


def get_query_results(query):
    '''Establishes a connection to the database and runs a given SELECT query'''
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def most_popular_articles():
    '''Display the 3 most popular articles of all time'''
    query = ("select title, count(path) as views from articles join log on "
             "articles.slug = substring(path from 10) group by title order by "
             "views desc limit 3;")
    popular_articles = get_query_results(query)
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
    popular_authors = get_query_results(query)
    print "\nThe most popular authors of all time are: \n"
    # loop through tuple, add to the print statement and
    # convert tuple to string
    for row in popular_authors:
        print "{0} - {1} views".format(*row)
    print "\n\n"


def error_request():
    '''Display the day on which more than 1% of requests led to errors'''
    query = ("select time::date as day, cast(count(substring('404 NOT FOUND' "
             "from status)) * 100.0 / count(*) as decimal(10,1)) as error "
             "from log group by day having "
             "count(substring('404 NOT FOUND' from status)) * 100.0 / "
             "count(*) > 1;")
    error_requests = get_query_results(query)
    print "\nThe day with request errors more than 1%: \n"
    # loop through tuple, add to the print statement and
    # convert tuple to string
    for row in error_requests:
        print "{0} - {1}% errors\n".format(*row)

''' make calls to the function in order to query the news database
 present the results'''
most_popular_articles()
most_popular_authors()
error_request()
