# Log Analysis Project

This python script queries a news database with 3 tables:
 - articles
 - authors
 - log

The script returns answers to the following queries:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Pre-requisites

You will need to have the following ready before you can run this script: 
The project makes use of the Linux-based virtual machine (VM)

1. [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. [Install Vagrant](https://www.vagrantup.com/downloads.html)
3. [Download the configuration for the VM](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
3. [Download the news database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
4. Python(preferable Python 3)
5. Git bash terminal

After install 1, 2 and 3 above, from your terminal, inside the **vagrant subdirectory/configuration**(from 3 above), run the command **vagrant up**. This will allow Vagrant to download the Linux operating system and install it.

Run **vagrant ssh** when **vagrant up** is done in order to log in to your Linux VM.

The final step will be to **cd** into your **/vagrant** directory

## How to run the script

1. Clone the newsdb.py file into a folder on your local machine.
2. Ensure you have the newsdata.sql file in the same folder(the vagrant folder) as the newsdb.py script.
3. Run **psql newsdata.sql** to access the news database.
4. Finally, run **python newsdb.py** for the script to display the results.