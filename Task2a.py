from pyowm.owm import OWM
owm = OWM(api_key='b7409f973b88716323ca9dd50d84b2c2')
mgr = owm.weather_manager()

reg = owm.city_id_registry()
list_of_locations = reg.locations_for('kazan', country='RU')
kazan = list_of_locations[0]
lat = kazan.lat   # 55.788738
lon = kazan.lon   # 49.122139

one_call = mgr.one_call(lat, lon, units = 'metric')
daily_weather = one_call.forecast_daily

feels_evening_temp_list = list()
pressure_list = list()

print('Average feels evening temperature and pressure for the next 5 days (including today) in Kazan:')
for i in range(5):
    date = daily_weather[i].reference_time('iso')

    feels_evening_temp = daily_weather[i].temperature('celsius').get('feels_like_eve')
    feels_evening_temp_list.append(feels_evening_temp)

    pressure = daily_weather[i].pressure['press']
    pressure_list.append(pressure)

    print('Date: {0}\t Evening temp.: {1} celsius\t Pressure: {2}'.format(date, feels_evening_temp, pressure))

avg_feels_evening_temp = sum(feels_evening_temp_list) / len(feels_evening_temp_list)
min_pressure = min(pressure_list)

print('\nAverage feels evening temperature: {0} celsius'.format(avg_feels_evening_temp))
print('Minimum pressure.: {}'.format(min_pressure))