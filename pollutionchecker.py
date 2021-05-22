import tkinter as tk  # Importing Tkinter for GUI
import matplotlib.pyplot as plt  # Importing matplotlib for making Pie-Chart
import requests  # Importing requests to access url

root = tk.Tk()
root.geometry('500x600')  # Creating window of Live Pollution Detector
root.title('Live Pollution Detector')  # Title of the window
root.configure(bg='black')  # Background of window
name_var = tk.StringVar()


def submit():  # Submit Function
    city = name_entry.get()  # Taking input of city from user
    url = 'http://api.waqi.info/feed/' + city + '/?token='  # URL of API
    api_key = '37f96394ffe8b6cca1110af3d8270604c711c688'  # Key to access API
    main_url = url + api_key  # Main URL
    r = requests.get(main_url)  # Accessing the URL
    data = r.json()['data']  # Fetching data in variable
    aqi = data['aqi']  # Air quality Index
    iaqi = data['iaqi']  # Individual Air Quality Index

    del iaqi['p']  # Deleting unused information

    # Assigning information to individual variable
    temperature = iaqi.get('t', 'Not Available')
    humidity = iaqi.get('h', 'Not Available')
    dew = iaqi.get('dew', 'Not Available')
    no2 = iaqi.get('no2', 'Not Available')
    o3 = iaqi.get('o3', 'Not Available')
    so2 = iaqi.get('so2', 'Not Available')
    pm10 = iaqi.get('pm10', 'Not Available')
    pm25 = iaqi.get('pm25', 'Not Available')

    # Printing the information in list form
    list1.insert(1, f'{city.upper()} AQI :{aqi} µg/m³')
    list1.insert(2, 'Individual Air quality')
    list1.insert(3, f'Dew :{dew}')
    list1.insert(4, f'NO2 :{no2} µg/m³')
    list1.insert(5, f'Ozone :{o3} µg/m³')
    list1.insert(6, f'Sulphur :{so2} µg/m³')
    degree_sign = u"\N{DEGREE SIGN}"
    list1.insert(7, f'Temperature :{temperature} {degree_sign}C ')
    list1.insert(8, f'Humidity :{humidity} g/kg')
    list1.insert(9, f'pm10 :{pm10}g/m³')
    list1.insert(10, f'pm25 :{pm25}g/m³')

    """Plotting pollutants PIE-CHART"""

    pollutants = [i for i in iaqi]
    values = [i['v'] for i in iaqi.values()]

    # Exploding the first slice
    explode = [0 for i in pollutants]
    mx = values.index(max(values))  # explode 1st slice
    explode[mx] = 0.1

    plt.figure(figsize=(8, 6))  # Size of the figure
    plt.pie(values, labels=pollutants, explode=explode, autopct='%1.1f%%', shadow=True)



    plt.title('Air pollutants and their probable amount in atmosphere of {} and the pollution level is {}'.format(city.upper(), level))  # Title of Pie-Chart

    plt.axis('equal')
    plt.show()  # Showing the Pie-Chart
    name_var.set("")


name_label = tk.Label(root, text='Enter the name of city', font=('calibre', 10, 'bold'), padx=3)  # Label Of City
name_label.place(x=175, y=110)
name_entry = tk.Entry(root, width=30, textvariable=name_var, font=('calibre', 10, 'normal'))  # Input of City name
name_entry.place(x=140, y=150)
sub_btn = tk.Button(root, text='Submit', command=submit)  # Submit Button
sub_btn.place(x=220, y=200)
list1 = tk.Listbox(root, width=50, height=10)  # Details about the city
list1.place(x=75, y=250)

root.mainloop()  # Mainloop for continuous execution
