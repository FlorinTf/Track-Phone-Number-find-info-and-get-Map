from tkinter import *
from geopy.geocoders import Nominatim
import phonenumbers
from opencage.geocoder import OpenCageGeocode
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from timezonefinder import TimezoneFinder
from datetime import datetime
import tkintermapview
import pytz


root =Tk()
root.title('Phone Number Tracker')
root.geometry('472x700+800+65')
root.resizable(False,False)
background = '#002B44'
empty = '. . . . . . . . . . . . . . . . . . . . . . .'
x='5'
x2='160'
map_count = 0

root.config(background=background)

def search(geocoder=geocoder):
    global lat
    global lng
    global location
    global map_count

    map_count = 0
    enter_number=entry.get()
    pepnumber=phonenumbers.parse(enter_number)

    location_1 = geocoder.description_for_number(pepnumber,'en')

    # carier
    service_pro = phonenumbers.parse(enter_number)
    if carrier.name_for_number(service_pro,'en') == '':
        phone_carrier_ans.config(text='Just for mobile phone')
    else:
        phone_carrier_ans.config(text=carrier.name_for_number(service_pro,'en'))
    # Time Zone
    number=phonenumbers.parse(enter_number)
    time=timezone.time_zones_for_number(number)
    time_zone.config(text=time)

    key = '05f849c9bc0141d8ac2465fdfe7c39'
    geocoder = OpenCageGeocode(key)
    query = str(location_1)
    result = geocoder.geocode(query)
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    gps_button.config(text=f'{lat}, {lng}')
    country_s = result[0]['components']['country']
    country_ans.config(text=country_s)
    continent = result[0]['components']['continent']
    continent_ans.config(text=continent)
    try:
        country_code = result[0]['components']['ISO_3166-1_alpha-2']
        country_code_ans.config(text=country_code)
    except:
        pass
    currency = result[0]['annotations']['currency']['iso_code']
    symbol = result[0]['annotations']['currency']['symbol']
    currency_ans.config(text=(f'{currency},  {symbol}'))
    currency_name = result[0]['annotations']['currency']['name']
    currency_name_ans.config(text=currency_name)
    # wikidata = result[0]['annotations']['wikidata']

    #time showing in phone
    geolocator = Nominatim(user_agent='geoapiEx')
    location= geolocator.geocode(location_1,language='en')
    location_ans.config(text=location)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime('%I:%M.%p')
    time_zone_ans.config(text=current_time)

def map():
    global map_count
    global top

    if map_count == 0:
        top = Toplevel()
        top.title('Phone location')
        top.geometry('800x600+50+50')
        top.resizable(False,False) 
        map=tkintermapview.TkinterMapView(top,width=800,height=600,corner_radius=0)
        map.set_position(location[1][0],location[1][1],marker=True,text=f'The phone is located in {location}')
        map.set_zoom(7)
        map.pack()
        map_count +=1

#img
img = PhotoImage(file='world_new.png')
Label(root,image=img,background=background).place(x=0,y=0)

# Entry phone number
entry=StringVar()
enter_number = Entry(root,textvariable=entry,width=18,bd=0,font=('arial',20,'bold'))
enter_number.place(x=100,y=295)

#button
Search_image=PhotoImage(file='search.png')
search_btn=Button(image=Search_image,borderwidth=0,cursor='hand2',bd=0,font=('arial',16)
                  ,background=background,activebackground=background,command=search)
search_btn.place(x=89,y=350)

# INFO
#Phone Carrier
phone_carrier=Label(root,text='Phone Carrier:',bg=background,fg='white',font=('arial',12,'bold'))
phone_carrier.place(x=x,y=410)
phone_carrier_ans=Label(root,text='Just for mobile phone',bg=background,fg='white',font=('arial',12,'bold'))
phone_carrier_ans.place(x=x2,y=410)

# City
location=Label(root,text='Location:',bg=background,fg='white',font=('arial',12,'bold'))
location.place(x=x,y=440)
location_ans=Label(root,text=empty,bg=background,fg='white',font=('arial',12,'bold'))
location_ans.place(x=x2,y=440)

# Latitude and longitude
gps_button = Button(text='Country for mobile & City for landline',borderwidth=5,cursor='hand2',
                    bd=0,font=('arial',12,'bold'),bg=background,fg='white',command=map)
gps_button.place(x=x2,y=470)
latitude_longitude=Label(root,text='Lat & Lng:',bg=background,fg='white',font=('arial',12,'bold'))
latitude_longitude.place(x=x,y=470)

# Country
country=Label(root,text='Country:',bg=background,fg='white',font=('arial',12,'bold'))
country.place(x=x,y=500)
country_ans=Label(root,text=empty,bg=background,fg='white',font=('arial',12,'bold'))
country_ans.place(x=x2,y=500)

# Continent
continent=Label(root,text='Continent:',bg=background,fg='white',font=('arial',12,'bold'))
continent.place(x=x,y=530)
continent_ans=Label(root,text=empty,bg=background,fg='white',font=('arial',12,'bold'))
continent_ans.place(x=x2,y=530)

# Time Zone
time_zone=Label(root,text='Time Zone:',bg=background,fg='white',font=('arial',12,'bold'))
time_zone.place(x=x,y=560)
time_zone_ans=Label(root,text=empty,bg=background,fg='white',font=('arial',12,'bold'))
time_zone_ans.place(x=x2,y=560)

# Country Code
country_code=Label(root,text='Country Code:',bg=background,fg='white',font=('arial',12,'bold'))
country_code.place(x=x,y=590)
country_code_ans=Label(root,text=empty,bg=background,fg='white',font=('arial',12,'bold'))
country_code_ans.place(x=x2,y=590)

# Currency
currency=Label(root,text='Currency & symbol:',bg=background,fg='white',font=('arial',12,'bold'))
currency.place(x=x,y=620)
currency_ans=Label(root,text=empty,bg=background,fg='white',font=('arial',12,'bold'))
currency_ans.place(x=x2,y=620)

# Currency
currency_name=Label(root,text='Currency name:',bg=background,fg='white',font=('arial',12,'bold'))
currency_name.place(x=x,y=650)
currency_name_ans=Label(root,text=empty,bg=background,fg='white',font=('arial',12,'bold'))
currency_name_ans.place(x=x2,y=650)

root.mainloop()
