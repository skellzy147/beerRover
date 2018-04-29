from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import serial
app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0')
@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    messageBody = request.form['Body']
    listOfWords = messageBody.split()
    print(listOfWords)
    i = 0
    while i < len(listOfWords):
      sendMePls(listOfWords[i], listOfWords[i+1])
      print('{0}, {1} :'.format(listOfWords[i], listOfWords[i+1]))
      i+=2
 
    messageReply = 'Succ'
    # Add a message
    resp.message(messageReply)
 
    return str(resp)
 
def sendMePls(arg1, arg2):
   arg1 = arg1.lower()
   if arg1 == 'forward':
      ser.write(bytearray([0, int(arg2)]))
      print('{1},{0}'.format(arg1, arg2))
   elif arg1 == 'back':
      ser.write(bytearray([1, int(arg2)]))
      print('{1},{0}'.format(arg1, arg2))
   elif arg1 == 'left':
      ser.write(bytearray([3, int(arg2)]))
      print('{1},{0}'.format(arg1, arg2))
   elif arg1 == 'right':
      ser.write(bytearray([2, int(arg2)]))
      print('{1},{0}'.format(arg1, arg2))
   elif arg1 == 'lift':
      ser.write(bytearray([5, int(arg2)]))
      print('{1},{0}'.format(arg1, arg2))
   elif arg1 == 'grab':
      ser.write(bytearray([4, int(arg2)]))
      print('{1},{0}'.format(arg1, arg2))
   return
 
if __name__ == "__main__":
    app.run(debug=True)