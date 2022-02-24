import requests
import time
from datetime import datetime,timedelta

person_age=18
area_pincode=["831012"]
total_days=1
print_flag='Y'

print("Start searching for covid vaccine slot !!!")

current=datetime.today()
form=[current+timedelta(days=i) for i in range(total_days)]
correct_date=[i.strftime("%d-%m-%y") for i in form]

while True:
    i=0
    for find_code in area_pincode:
        for enter_date in correct_date:
            url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date{}".format(find_code,enter_date)
            requirements={
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,Like Gecko) Chrome/56.0.2924.76 Safari/537.36'
            }
            final_op=requests.get(url, headers=requirements)

            if final_op.ok:
                file_json=final_op.json()

                flag=False
                if file_json["centers"]:
                    if(print_flag.lower()=="y"):

                        for place in file_json["centers"]:
                            for availability in place["sessions"]:
                                if(availability["min_age_limit"]<=person_age and availability["available_capacity"]>0):
                                    print('The pincode for which you are finding is:'+find_code)
                                    print('It is available in: {}'.format(enter_date))
                                    print("Name of the hospital and destination is :",place["name"])
                                    print("Name for the block is :",place["block_name"])
                                    print("Price of the vaccine is :", place["fee_type"])
                                    print("Availability status of the vaccine is",availability["available_capacity"])

                                    if(availability["vaccine"] != ''):
                                        print("The type of vaccine is :",availability["vaccine"])
                                    i=i+1
                                else:
                                    pass
                    else:
                            pass
                else:
                    print("I found no response !!!")
            if(i==0):
                print('Right now no vaccine slots are not available !...Try after some time')
            else:
                print("The search is finished !!")
            date_now=datetime.now()+ timedelta(minutes=1)

            while datetime.now()<date_now:
                time.sleep(1)