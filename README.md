# CSV SCRAPER

La funcionabilidad de este modulo es escrapear datos de un archivo csv con una estructura especifica, dividido en 14 secciones donde cada seccion tiene sus respectivos data frames (Estructura de datos en Pandas)

### Requerimientos
Este modulo requiere que los siguientes paquetes esten instalados.
- pandas
- numpy
- csv

### Importacion del modulo
Para usar este modulo debemos llevar el directorio de este al mismo nivel del archivo donde lo importaremos.

para importar importar el modulo:

```py
from csv_scraper import csv_scraper as scrp
```
para almacenar los datos ya procesados en formato diccionario
```py
data = scrp.csv_scraper('data.csv')
```

Ahora podemos accesar a los datos atravez de esta variable llamada `data`



### Accesibilidad a los datos

Podemos acceder a la informacion almacenada en `data` atravez de 14 llaves que estan ya reservadas. 

| Nombre | Numero de DataFrames |
| ------ | ------ |
| IPRCurveData | 2|
| ZPlotData | 1 |
| VFDData | 4 |
| BasePumpCurveData |2 |
| OperatingFrequencyPumpCurveData | 2 |
| DeratedOperatingFrequencyPumpCurveData | 2 |
| OperatingFrequencyInsituPumpCurveData | 2 |
| DeratedOperatingFrequencyInsituPumpCurveData | 2 |
| OperatingPointAnalysisData | 5 |
| FunnelCurves | 10 |
| TornadoCurveData |8 |
| OpportunitiesData | 1 |
| GainsData | 1 |
| PredictionsData | 1 |


### Acceder al formato de salida de cada llave
```py
print(data['FunnelCurves'][0])
```