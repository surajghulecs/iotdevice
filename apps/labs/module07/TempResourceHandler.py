'''
Created on Mar 18, 2019
@author: Suraj
'''
import collections

CodeItem = collections.namedtuple('CodeItem', 'number name')
class Codes(object):
    
    ERROR_LOWER_BOUND = 128
    EMPTY = CodeItem(number = 0, name='EMPTY')
    GET = CodeItem(1, 'GET')
    POST = CodeItem(2, 'POST')
    PUT = CodeItem(3, 'PUT')
    DELETE = CodeItem(4, 'DELETE')
    
    CREATED = CodeItem(65, 'CREATED')
    DELETED = CodeItem(66, 'DELETED')
    VALID = CodeItem(67, 'VALID')
    CHANGED = CodeItem(68, 'CHANGED')
    CONTENT = CodeItem(69, 'CONTENT')
    CONTINUE = CodeItem(95, 'CONTINUE')
    
    BAD_REQUEST = CodeItem(128, 'BAD_REQUEST')
    FORBIDDEN = CodeItem(131, 'FORBIDDEN')
    NOT_FOUND = CodeItem(number = 132, name ='NOT_FOUND')
    METHOD_NOT_ALLOWED = CodeItem(133, 'METHOD_NOT_ALLOWED')
    NOT_ACCEPTABLE = CodeItem(134, 'NOT_ACCEPTABLE')
    REQUEST_ENTITY_INCOMPLETE = CodeItem(136, 'REQUEST_ENTITY_INCOMPLETE')
    PRECONDITION_FAILED = CodeItem(140, 'PRECONDITION_FAILED')
    REQUEST_ENTITY_TOO_LARGE = CodeItem(141, 'REQUEST_ENTITY_TOO_LARGE')
    UNSUPPORTED_CONTENT_FORMAT = CodeItem(143, 'UNSUPPORTED_CONTENT_FORMAT')
    
    INTERNAL_SERVER_ERROR = CodeItem(160, 'INTERNAL_SERVER_ERROR')
    NOT_IMPLEMENTED = CodeItem(161, 'NOT_IMPLEMENTED')
    BAD_GATEWAY = CodeItem(162, 'BAD_GATEWAY')
    SERVICE_UNAVAILABLE = CodeItem(163, 'SERVICE_UNAVAILABLE')
    GATEWAY_TIMEOUT = CodeItem(164, 'GATEWAY_TIMEOUT')
    PROXY_NOT_SUPPORTED = CodeItem(165, 'PROXY_NOT_SUPPORTED')


from coapthon.resources.resource import Resource
import coapthon.defines as defines
from labs.common import SensorData
from coapthon.messages import request
class TempResourceHandler(Resource):
    '''
    This is the Python implementation of the custom CoAP resource on CoAP server.
    This class defines the functions that specify how a CoAP request should 
    be handled and what response should be provided based on request and 
    condition of the resource on the server. 
    '''
    rt = request #instance of the request object
    
    def __init__(self, name_in="TemperatureResource", coapServer_in=None):
        '''
        This is the default constructor. This is called on the creation of the 
        class object.
        @param name_in: Srting - default is set to TemperatureResource
        @param coapServer_in: CoAP Server
        resource is initiated with required parameters
        sensorData is declared without initiating
        '''
        
        super(TempResourceHandler, self).__init__(name_in, coapServer_in)
        self.sensorData = None
    
    def render_GET_advanced(self, request, response):
        '''
        This function defines the action on receiving "GET" request.
        Based on the situation i.e. if there exists the data,  it would send back
        JSON formatted object in the response. If not, it would response with 
        "NOT FOUND" response code and message.
        '''
        
        if self.sensorData == None:
            response.code = Codes.NOT_FOUND.number
            response.payload = (defines.Content_types["text/plain"], "Object doesn't exist.")
        else:
            response.code = Codes.CONTENT.number
            response.payload = (defines.Content_types["application/json"], self.sensorData.fromSensortoJson(self.sensorData))
        return self, response
        
    def render_POST_advanced(self, request, response):
        '''
        This function defines the action on receiving "POST" request.
        We use POST to initiate the object and assign the first set of values 
        provided by the client. 
        Based on the situation i.e. if there doesn't exists the data, only then 
        it would successfully create a new object of the class and assign the 
        values and respond with "CREATED" response code.
        Otherwise it would send the "BAD REQUEST" response code.
        '''
        
        if self.sensorData != None:
            response.code = Codes.BAD_REQUEST.number
            response.payload = (defines.Content_types["text/plain"],"Object already exists")
        else:
            self.sensorData = SensorData.SensorData()
            self.rt = request
            print(self.rt.payload)
            self.sensorData.jsonToSensorData(self.rt.payload)
            response.code = Codes.CREATED.number
            response.payload = (defines.Content_types["text/plain"], "Object is created successfully")
        return self, response
        
    def render_PUT_advanced(self, request, response):
        '''
        This function defines the action on receiving "PUT" request.
        Based on the situation i.e. if there exists the data, it would update the
        object with new data and respond with "CHANGED" response code. Otherwise
        it would respond with "BAD REQUEST" response code and message.
        '''
        
        if self.sensorData == None:
            response.code = Codes.BAD_REQUEST.number
            response.payload = (defines.Content_types["text/plain"], "Object doesn't have any data")
        else:
            self.rt = request
            self.sensorData.jsonToSensorData(self.rt.payload)
            response.code = Codes.CHANGED.number
            response.payload = (defines.Content_types["text/plain"], "Object is updates successfully")    
        return self, response
        
    def render_DELETE_advanced(self, request, response):        
        '''
        This function defines the action on receiving "DELETE" request.
        Based on the situation i.e. if there exists the data,  it would delete
        the object, meaning set it to null and respond with 'DELETE' response
        code. Otherwise it would respond with 'BAD REQUEST' response code and
        message.
        '''
        
        if self.sensorData == None:
            response.code = Codes.BAD_REQUEST.number
            response.payload = (defines.Content_types["text/plain"], "Object doesn't exist to be deleted")
        else:
            self.sensorData = None
            response.code = Codes.DELETED.number
            response.payload = (defines.Content_types["text/plain"], "Object deleted successfully")
        return self, response