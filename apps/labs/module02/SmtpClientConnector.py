'''
Created on Jan 21, 2019
@author: suraj
'''
import labs.common.ConfigConst as ConfigConst
import labs.common.ConfigUtil as ConfigUtil
import smtplib
from email.mime.text import MIMEText as mimeText
from email.mime.multipart import MIMEMultipart as mimeMultipart

class SmtpClientConnector():
    
    '''
    Constructor of SmtpClientConnector
    Loads the Configuration file ConnectedDevicesConfig.props
    '''
    def __init__(self):  
        self.config = ConfigUtil.ConfigUtil('../../../config/data/ConnectedDevicesConfig.props')  
        self.config.loadConfig()     
        print('Configuration data...\n' + str(self.config))
    
    '''
    Publishes the trigger email
    @param topic - String value. Subject of the email
    @param data: - String value. Email body
    '''     
    def publishMessage(self, topic, data):  
        host = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY)  
        port = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY)  
        fromAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY)  
        toAddr = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)  
        authToken = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
         
        msg = mimeMultipart()           # object of mimeMultipart class
        msg['From'] = fromAddr          # email id from which we want to send email alert. Taken from ConnectedDevicesConfig.props
        msg['To'] = toAddr              # email id to which we want to send email alert. Taken from ConnectedDevicesConfig.props
        msg['Subject'] = topic      
        msgBody = str(data)          
         
        msg.attach(mimeText(msgBody))       
        msgText = msg.as_string()                       # send e-mail notification  
        smtpServer = smtplib.SMTP_SSL(host, port)       # connects to specified host and port number
        smtpServer.ehlo()                               # initial hello message
        smtpServer.login(fromAddr, authToken)           # logon to specified email id and password
        smtpServer.sendmail(fromAddr, toAddr, msgText)  # send email  
        smtpServer.close()                              # closes the connection
        
        
