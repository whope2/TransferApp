# TransferApp

Try my TransferApp hosted on a AWS EC2 instance:

Transfer a photo:
http://52.54.114.11

View the history of transfers:
http://52.54.114.11/stat

TransferApp implements a web service using Python/Flask framework, hosted on an EC2 instance on AWS. Two json files are implemented as database at backend to store new transfer activities.

Code can be used unchanged for testing.

Before deploying on AWS, change the IP and port number as follows:
App.Run(host='0.0.0.0',port=80)

Enjoy!
