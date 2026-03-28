# Proyecto-EDA Python
## Objetivo del proyecto
Realizar un análisis exploratorio de los datos contenidos en los archivos bank-additional.csv y customer-details.xlsx

## Archivos de datos
Estos conjuntos de datos están relacionados con campañas de marketing directo de una institución bancaria portuguesa. Las campañas de marketing se basaron en llamadas telefónicas. A menudo, se requería más de un contacto con el mismo cliente para determinar si el producto (depósito a plazo bancario) sería suscrito o no. Las columnas que tenemos en el primer dataset ('bank-additional.csv') son:  

●	**age**: La edad del cliente.  
●	**job**: La ocupación o profesión del cliente.  
●	**marital**: El estado civil del cliente.  
●	**education**: El nivel educativo del cliente.  
●	**default**: Indica si el cliente tiene algún historial de incumplimiento de pagos (1: Sí, 0: No).  
●	**housing**: Indica si el cliente tiene un préstamo hipotecario (1: Sí, 0: No).  
●	**loan**: Indica si el cliente tiene algún otro tipo de préstamo (1: Sí, 0: No).  
●	**contact**: El método de contacto utilizado para comunicarse con el cliente.  
●	**duration**: La duración en segundos de la última interacción con el cliente.  
●	**campaign**: El número de contactos realizados durante esta campaña para este cliente.  
●	**pdays**: Número de días que han pasado desde la última vez que se contactó con el cliente durante esta campaña.  
●	**previous**: Número de veces que se ha contactado con el cliente antes de esta campaña.  
●	**poutcome**: Resultado de la campaña de marketing anterior.  
●	**emp.var.rate**: La tasa de variación del empleo.  
●	**cons.price.idx**: El índice de precios al consumidor.  
●	**cons.conf.idx**: El índice de confianza del consumidor.  
●	**euribor3m**: La tasa de interés de referencia a tres meses.  
●	**nr.employed**: El número de empleados.  
●	**y**: Indica si el cliente ha suscrito un producto o servicio (Sí/No).  
●	**date**: La fecha en la que se realizó la interacción con el cliente.  
●	**contact_month**: Mes en el que se realizó la interacción con el cliente durante la campaña de marketing.  
●	**contact_year**: Año en el que se realizó la interacción con el cliente durante la campaña de marketing.  
●	**id_**: Un identificador único para cada registro en el dataset.  

El segundo set de datos ('customer-details.xlsx') es un archivo Excel que nos da información sobre las características demográficas y comportamiento de compra de los clientes del banco. Este Excel consta de 3 hojas de trabajo diferentes, en cada una de ellas tenemos los clientes que entraron en el banco en diferentes años. Sus columnas son:  

●	**Income**: Representa el ingreso anual del cliente en términos monetarios.  
●	**Kidhome**: Indica el número de niños en el hogar del cliente.  
●	**Teenhome**: Indica el número de adolescentes en el hogar del cliente.  
●	**Dt_Customer**: Representa la fecha en que el cliente se convirtió en cliente de la empresa.  
●	**NumWebVisitsMonth**: Indica la cantidad de visitas mensuales del cliente al sitio web de la empresa.  
●	**ID**: Identificador único del cliente.  

## Limpieza de datos

1. Normalización de nombres y formatos
Se estandarizaron los nombres de las columnas a minúsculas y se sustituyeron los puntos por guiones bajos, lo que facilita la manipulación del DataFrame y evita errores en el análisis.
Asimismo, todas las columnas de tipo object se transformaron a minúsculas para asegurar consistencia en las categorías.

2. Corrección de tipos de datos
Varias columnas numéricas aparecían como cadenas con comas decimales. Se corrigieron y transformaron a tipo float, incluyendo:

- cons_price_idx
- cons_conf_idx
- euribor3m

La columna age se convirtió a entero y se eliminaron los registros con valores nulos, ya que representaban un volumen significativo pero no aportaban información útil.

3. Limpieza y estandarización de variables categóricas
Se corrigieron categorías inconsistentes:
- job: se reemplazó admin. por administrative y se creó la categoría unknown para valores nulos.
- marital: se imputaron valores nulos como unknown.
- education: se sustituyeron puntos por guiones bajos y se imputaron valores nulos como unknown.
- Las columnas default, housing, loan y y se normalizaron para contener únicamente yes, no o unknown, descartando la conversión a booleano para preservar la categoría de desconocido.

4. Corrección de la columna de fecha y reconstrucción de mes y año
La columna date se transformó a tipo fecha utilizando el formato español.
Las columnas latitude y longitude, que no tenían sentido en el contexto del dataset, fueron reemplazadas por:
-contact_month
-contact_year

extraídos directamente de la fecha.
Finalmente, la columna date se eliminó al no aportar valor adicional al análisis.

5. Creación de nuevas variables
Se generó la columna age_group para segmentar a los clientes en rangos de edad:
- 18–30
- 31–45
- 46–60
- 60+
Esta variable facilita el análisis demográfico y la interpretación de patrones de conversión.

6. Integración con el archivo customer-details
El archivo Excel presentaba datos consistentes, por lo que se integró sin necesidad de limpieza adicional.
La unión con el dataset principal permitió enriquecer el análisis con información demográfica y de comportamiento del cliente.

## Conclusión Final del Análisis Exploratorio de Datos (EDA)
El análisis exploratorio realizado sobre los datos de la campaña de marketing del banco permite comprender con detalle los factores que influyen en la suscripción del producto ofrecido. A través de la limpieza, transformación y exploración de las variables numéricas y categóricas, se identificaron patrones relevantes tanto en el comportamiento de los clientes como en la efectividad de las campañas previas.

1. Distribución general de los clientes
El conjunto de datos presenta una amplia variedad de perfiles, con predominio de clientes de mediana edad, niveles educativos intermedios y profesiones administrativas, técnicas y de servicios. La variable objetivo (y) está desbalanceada, con una mayoría de clientes que no suscriben el producto, lo que es habitual en campañas de marketing.

2. Variables numéricas
Entre las variables numéricas, la duración de la llamada destaca como el factor más correlacionado con la conversión. Las llamadas más largas tienden a asociarse con una mayor probabilidad de suscripción, lo que sugiere que el tiempo de interacción es clave para cerrar la venta.

3. Variables categóricas
Las variables categóricas revelan diferencias significativas entre grupos:

- Profesión (job):  
    Aunque los estudiantes y jubilados presentan las tasas de conversión más altas, su volumen es reducido. En términos absolutos, los administrativos y técnicos aportan la mayor cantidad de conversiones debido a su gran presencia en el dataset.

- Nivel educativo (education):  
    Los clientes sin educación muestran la tasa más alta, pero representan un grupo muy pequeño. Los niveles educativos más comunes —secundaria, cursos profesionales y estudios universitarios— presentan tasas moderadas, pero concentran la mayoría de las conversiones totales.

- Resultado de campañas previas (poutcome):  
    Los clientes con success previo tienen una probabilidad muy alta de volver a convertir, aunque son pocos. El grupo nonexistent, que nunca había sido contactado, tiene la tasa más baja pero aporta la mayor parte de las conversiones debido a su tamaño.

- Método de contacto (contact):  
    El contacto por teléfono móvil (cellular) es claramente más efectivo que el teléfono fijo (telephone).

4. Conclusión general
El EDA evidencia que la conversión no depende de una única variable, sino de la interacción entre características personales, contexto económico y calidad del contacto. La duración de la llamada emerge como el factor más determinante, mientras que variables como profesión, educación y resultado de campañas previas permiten identificar segmentos con mayor potencial.

















