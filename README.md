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

TransferApp implements a web service using Python/Flask framework, hosted on an EC2 instance on AWS. Two json files are implemented as database at backend to store new transfer activities.

Code can be used unchanged for testing.

For debugging, use the default localhost and port 5000:
App.Run(port=5000,debug=False)

Before deploying on AWS, change the IP and port number as follows:
App.Run(host='0.0.0.0',port=80)

Enjoy!
