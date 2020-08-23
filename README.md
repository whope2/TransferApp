# TransferApp

Try my TransferApp hosted on a AWS EC2 instance:

Transfer a photo or Upload a quote or Upload a new word or submit a new note:
http://52.54.114.11

View the history of transfers and uploaded quotes, words, and notes:
http://52.54.114.11/stat

View Picture of The Day:
http://52.54.114.11/pictureoftheday

View Quote of The Day:
http://52.54.114.11/quoteoftheday

View Word of The Day:
http://52.54.114.11/wordoftheday

View Notes:
http://52.54.114.11/stat

Plot line graphs using Python matplotlib backend. X axis supports both numeric and datetime data types. Y axis supports accumulated values.  

TransferApp implements a web service using Python/Flask framework, hosted on an EC2 instance on AWS. Multiple json files are implemented as database at backend to store new photo transfer and quote and word update activities.

Backend json files are automatically backed up after each transaction. 

For debugging and testing, use the default localhost and port 5000:
App.Run(port=5000,debug=False)

For production on AWS, change the IP and port number as follows:
App.Run(host='0.0.0.0',port=80)

Enjoy!
