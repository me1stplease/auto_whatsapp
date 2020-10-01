from twilio.rest import Client 
import schedule
import time
 
account_sid = 'ACfb22616c39a471068938089ba2943ec8' 
auth_token = 'a5d9d127439c6b99bb3db86542600299' 
client = Client(account_sid, auth_token) 

def job():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body= "Gud mrng :)\nHave a lovely Day. <3",      
                                to='whatsapp:+917209291966' 
                            ) 
    
    print(message.sid)




schedule.every().day.at("06:30").do(job)
"""schedule.every().minutes.do(job)"""

while True :
    schedule.run_pending()
    time.sleep(1)