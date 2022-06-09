import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc = {'figure.figsize':(15,10)})
tide = pd.read_csv('./raw_csv/tide.csv', delimiter=';')
beach = pd.read_csv('./raw_csv/beach.csv', delimiter=';')
day_forecast = pd.read_csv('./raw_csv/day_forecast.csv', delimiter=';')
fact_size = pd.read_csv('./raw_csv/fact_size.csv', delimiter=';')
fact_texture = pd.read_csv('./raw_csv/fact_texture.csv', delimiter=';')
hour_forecast = pd.read_csv('./raw_csv/hour_forecast.csv', delimiter=';')
sea_condition_fact = pd.read_csv('./raw_csv/sea_condition_fact.csv', delimiter=';')
spot = pd.read_csv('./raw_csv/spot.csv', delimiter=';')
fact_shape = pd.read_csv('./raw_csv/fact_shape.csv', delimiter=';')



result = pd.merge(hour_forecast, day_forecast, on="iddayforecast")
result = pd.merge(result, beach, on="idbeach")
result = result.drop(columns=['idhourforecast','iddayforecast','idbeach','latitude','longitude','country','state','city'])
#result['time'] = pd.to_datetime(result['time'])

# Ordena pela data e salva em um novo DataFrame
result_ordenado = result.sort_values(by=['date', 'time'])

result_ordenado.head(10)
tidedf = pd.merge(tide, day_forecast, on="iddayforecast")
tidedf = pd.merge(tidedf, beach, on="idbeach")
tidedf = tidedf.drop(columns=['idtide','iddayforecast','idbeach','latitude','longitude','country','state','city'])
tidedf['time'] = pd.to_datetime(tidedf['time'])

# Ordena pela data e salva em um novo DataFrame
tidedf_ordenado = tidedf.sort_values(by='time')

tidedf_ordenado.head(5)
printed = hour_forecast.describe(include = 'all')
sns.boxplot(x='moon_phase', y='height', data=tidedf_ordenado)
plt.show()
day_forecast.head()
day_forecast['moon_phase'].value_counts()
sns.heatmap(day_forecast.corr(), annot=True)
plt.show()
sns.boxplot(x='moon_phase', y='maxtemp', data=day_forecast)
plt.show()
hour_forecast.head(1)
beach.head(1)


result_ordenado.hist(figsize=[25,15]);
sns.boxplot(x='moon_phase', y='height', data=tidedf_ordenado);

plt.show()