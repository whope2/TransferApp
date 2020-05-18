# TransferApp

Try my TransferApp hosted on a AWS EC2 instance:

Transfer a photo or Upload a quote:
http://52.54.114.11

View the history of transfers and uploaded quotes:
http://52.54.114.11/stat

View Picture of The Day:
http://52.54.114.11/pictureoftheday

View Quote of The Day:
http://52.54.114.11/quoteoftheday

TransferApp implements a web service using Python/Flask framework, hosted on an EC2 instance on AWS. Two json files are implemented as database at backend to store new photo transfer and quote update activities.

Backend json files are automatically backed up after each transaction. 

For debugging and testing, use the default localhost and port 5000:
App.Run(port=5000,debug=False)

For production on AWS, change the IP and port number as follows:
App.Run(host='0.0.0.0',port=80)

Enjoy!
