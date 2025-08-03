/* Tipo objeto que representa un FDI anual individual 
con dos atributos: año y porcentaje.*/

CREATE OR REPLACE TYPE fdi_anual_tipo AS OBJECT(
    anio NUMBER(4),
    fdi_porcentaje NUMBER(5,2)
    );
    
-- Tipo tabla anidada que permite almacenar múltiples FDI anuales por país.

CREATE OR REPLACE TYPE fdi_lista_tipo AS TABLE OF fdi_anual_tipo;


/*Tabla principal que almacena países junto con su lista de FDI (anidada) 
en estructura objeto-relacional.*/

CREATE TABLE fdi_pais_objeto(
    nombre_pais VARCHAR2(100),
    codigo_pais VARCHAR(10),
    fdi_anual fdi_lista_tipo
)

/* 
  Asocia la colección anidada 'fdi_anual' con una tabla de almacenamiento 
  físico ('fdi_anual_nt'). Esta instrucción es necesaria para que Oracle 
  gestione internamente los datos del tipo TABLE OF OBJECT.
*/

NESTED TABLE fdi_anual STORE AS fdi_anual_nt;


/*
  Se insertan los regitros en la tabla fdi_pais_objeto.
  Se especifica el país, su código y una colección anidada de objetos 
  fdi_anual_tipo que representan los valores históricos de FDI por año.
*/


-- España
INSERT INTO fdi_pais_objeto VALUES (
    'España',
    'ESP',
    fdi_lista_tipo(
        fdi_anual_tipo(2000.0, 6.77), fdi_anual_tipo(2001.0, 4.6), fdi_anual_tipo(2002.0, 5.55),
        fdi_anual_tipo(2003.0, 3.39), fdi_anual_tipo(2004.0, 2.36), fdi_anual_tipo(2005.0, 2.34),
        fdi_anual_tipo(2006.0, 2.61), fdi_anual_tipo(2007.0, 4.62), fdi_anual_tipo(2008.0, 4.53),
        fdi_anual_tipo(2009.0, 0.64), fdi_anual_tipo(2010.0, 2.56), fdi_anual_tipo(2011.0, 1.8),
        fdi_anual_tipo(2012.0, 1.57), fdi_anual_tipo(2013.0, 3.46), fdi_anual_tipo(2014.0, 2.32),
        fdi_anual_tipo(2015.0, 1.97), fdi_anual_tipo(2016.0, 3.62), fdi_anual_tipo(2017.0, 2.54),
        fdi_anual_tipo(2018.0, 4.47), fdi_anual_tipo(2019.0, 2.16), fdi_anual_tipo(2020.0, 2.92),
        fdi_anual_tipo(2021.0, 4.42), fdi_anual_tipo(2022.0, 4.53)
    )
);

COMMIT;

-- Irlanda 
INSERT INTO fdi_pais_objeto VALUES (
    'Iralanda',
    'IRL',
    fdi_lista_tipo(
        fdi_anual_tipo(2000.0, 25.73), fdi_anual_tipo(2001.0, 8.83), fdi_anual_tipo(2002.0, 22.8),
        fdi_anual_tipo(2003.0, 13.83), fdi_anual_tipo(2004.0, -5.46), fdi_anual_tipo(2005.0, 22.18),
        fdi_anual_tipo(2006.0, 9.51), fdi_anual_tipo(2007.0, 22.19), fdi_anual_tipo(2008.0, 8.45),
        fdi_anual_tipo(2009.0, 22.83), fdi_anual_tipo(2010.0, 17.0), fdi_anual_tipo(2011.0, 9.82),
        fdi_anual_tipo(2012.0, 25.56), fdi_anual_tipo(2013.0, 29.81), fdi_anual_tipo(2014.0, 39.32),
        fdi_anual_tipo(2015.0, 74.75), fdi_anual_tipo(2016.0, 26.1), fdi_anual_tipo(2017.0, 20.41),
        fdi_anual_tipo(2018.0, 20.38), fdi_anual_tipo(2019.0, 7.68), fdi_anual_tipo(2020.0, 8.08),
        fdi_anual_tipo(2021.0, 14.63), fdi_anual_tipo(2022.0, -6.49)
    )
);
COMMIT;

-- Unión Europea
INSERT INTO fdi_pais_objeto VALUES (
    'Unión Europea',
    'EUU',
    fdi_lista_tipo(
        fdi_anual_tipo(2000.0, 8.72), fdi_anual_tipo(2001.0, 4.96), fdi_anual_tipo(2002.0, 3.65),
        fdi_anual_tipo(2003.0, 2.95), fdi_anual_tipo(2004.0, 2.74), fdi_anual_tipo(2005.0, 6.12),
        fdi_anual_tipo(2006.0, 7.14), fdi_anual_tipo(2007.0, 9.99), fdi_anual_tipo(2008.0, 5.06),
        fdi_anual_tipo(2009.0, 3.96), fdi_anual_tipo(2010.0, 3.27), fdi_anual_tipo(2011.0, 5.68),
        fdi_anual_tipo(2012.0, 3.95), fdi_anual_tipo(2013.0, 3.89), fdi_anual_tipo(2014.0, 2.96),
        fdi_anual_tipo(2015.0, 6.23), fdi_anual_tipo(2016.0, 5.2), fdi_anual_tipo(2017.0, 3.97),
        fdi_anual_tipo(2018.0, 0.83), fdi_anual_tipo(2019.0, 3.69), fdi_anual_tipo(2020.0, 1.24),
        fdi_anual_tipo(2021.0, 3.76), fdi_anual_tipo(2022.0, 1.11)
    )
);
COMMIT;

-- Estados Unidos
INSERT INTO fdi_pais_objeto VALUES (
    'Estados Unidos de América',
    'USA',
    fdi_lista_tipo(
        fdi_anual_tipo(2000.0, 3.41), fdi_anual_tipo(2001.0, 1.63), fdi_anual_tipo(2002.0, 1.02),
        fdi_anual_tipo(2003.0, 1.02), fdi_anual_tipo(2004.0, 1.75), fdi_anual_tipo(2005.0, 1.09),
        fdi_anual_tipo(2006.0, 2.16), fdi_anual_tipo(2007.0, 2.39), fdi_anual_tipo(2008.0, 2.31),
        fdi_anual_tipo(2009.0, 1.11), fdi_anual_tipo(2010.0, 1.75), fdi_anual_tipo(2011.0, 1.69),
        fdi_anual_tipo(2012.0, 1.54), fdi_anual_tipo(2013.0, 1.71), fdi_anual_tipo(2014.0, 1.43),
        fdi_anual_tipo(2015.0, 2.8), fdi_anual_tipo(2016.0, 2.52), fdi_anual_tipo(2017.0, 1.94),
        fdi_anual_tipo(2018.0, 1.04), fdi_anual_tipo(2019.0, 1.47), fdi_anual_tipo(2020.0, 0.64),
        fdi_anual_tipo(2021.0, 2.01),fdi_anual_tipo(2022.0, 1.57)
    )
);
COMMIT;

-- Alemania
INSERT INTO fdi_pais_objeto VALUES (
        'Alemania',
        'DEU',
        fdi_lista_tipo(
            fdi_anual_tipo(2000.0, 12.61), fdi_anual_tipo(2001.0, 2.9), fdi_anual_tipo(2002.0, 2.44),
        fdi_anual_tipo(2003.0, 2.58), fdi_anual_tipo(2004.0, -0.72), fdi_anual_tipo(2005.0, 2.07),
        fdi_anual_tipo(2006.0, 2.87), fdi_anual_tipo(2007.0, 1.46), fdi_anual_tipo(2008.0, 0.81),
        fdi_anual_tipo(2009.0, 1.63), fdi_anual_tipo(2010.0, 2.48), fdi_anual_tipo(2011.0, 2.55),
        fdi_anual_tipo(2012.0, 1.82), fdi_anual_tipo(2013.0, 1.76), fdi_anual_tipo(2014.0, 0.44),
        fdi_anual_tipo(2015.0, 1.82), fdi_anual_tipo(2016.0, 1.64), fdi_anual_tipo(2017.0, 2.89),
        fdi_anual_tipo(2018.0, 4.0), fdi_anual_tipo(2019.0, 1.91), fdi_anual_tipo(2020.0, 4.49),
        fdi_anual_tipo(2021.0, 2.35), fdi_anual_tipo(2022.0, 1.51)
        )
    );
COMMIT;

-- FRANCIA
INSERT INTO fdi_pais_objeto VALUES (
        'Francia',
        'FRA',
        fdi_lista_tipo(
            fdi_anual_tipo(2000.0, 3.04), fdi_anual_tipo(2001.0, 3.66), fdi_anual_tipo(2002.0, 3.45),
        fdi_anual_tipo(2003.0, 2.31), fdi_anual_tipo(2004.0, 1.69), fdi_anual_tipo(2005.0, 3.88),
        fdi_anual_tipo(2006.0, 3.41), fdi_anual_tipo(2007.0, 3.15), fdi_anual_tipo(2008.0, 2.32),
        fdi_anual_tipo(2009.0, 0.68), fdi_anual_tipo(2010.0, 1.47), fdi_anual_tipo(2011.0, 1.54),
        fdi_anual_tipo(2012.0, 1.23), fdi_anual_tipo(2013.0, 1.19), fdi_anual_tipo(2014.0, 0.18),
        fdi_anual_tipo(2015.0, 1.77), fdi_anual_tipo(2016.0, 1.44),  fdi_anual_tipo(2017.0, 1.69),
        fdi_anual_tipo(2018.0, 2.79), fdi_anual_tipo(2019.0, 1.96), fdi_anual_tipo(2020.0, 0.73),
        fdi_anual_tipo(2021.0, 3.3), fdi_anual_tipo(2022.0, 3.92)
        )
    );
COMMIT;

-- Italia
INSERT INTO fdi_pais_objeto VALUES (
        'Italia',
        'ITA',
        fdi_lista_tipo(
            fdi_anual_tipo(2000.0, 1.15), fdi_anual_tipo(2001.0, 1.27), fdi_anual_tipo(2002.0, 1.34),
        fdi_anual_tipo(2003.0, 1.24),  fdi_anual_tipo(2004.0, 1.11), fdi_anual_tipo(2005.0, 1.97),
        fdi_anual_tipo(2006.0, 2.91), fdi_anual_tipo(2007.0, 2.97), fdi_anual_tipo(2008.0, -0.39),
        fdi_anual_tipo(2009.0, 0.75),  fdi_anual_tipo(2010.0, 0.46), fdi_anual_tipo(2011.0, 1.49),
        fdi_anual_tipo(2012.0, 0.0), fdi_anual_tipo(2013.0, 0.91), fdi_anual_tipo(2014.0, 0.78),
        fdi_anual_tipo(2015.0, 0.72), fdi_anual_tipo(2016.0, 1.36), fdi_anual_tipo(2017.0, 0.44),
        fdi_anual_tipo(2018.0, 2.11), fdi_anual_tipo(2019.0, 1.77), fdi_anual_tipo(2020.0, -0.89),
        fdi_anual_tipo(2021.0, 1.14), fdi_anual_tipo(2022.0, 2.98)
        )
    );
COMMIT;

-- Polonia
INSERT INTO fdi_pais_objeto VALUES (
        'Polonia',
        'POL',
        fdi_lista_tipo(
            fdi_anual_tipo(2000.0, 5.4), fdi_anual_tipo(2001.0, 2.96), fdi_anual_tipo(2002.0, 2.05),
        fdi_anual_tipo(2003.0, 2.46), fdi_anual_tipo(2004.0, 5.41), fdi_anual_tipo(2005.0, 3.6),
        fdi_anual_tipo(2006.0, 6.21), fdi_anual_tipo(2007.0, 5.83), fdi_anual_tipo(2008.0, 2.72),
        fdi_anual_tipo(2009.0, 3.18), fdi_anual_tipo(2010.0, 3.94), fdi_anual_tipo(2011.0, 3.57),
        fdi_anual_tipo(2012.0, 1.53), fdi_anual_tipo(2013.0, 0.26), fdi_anual_tipo(2014.0, 3.85),
        fdi_anual_tipo(2015.0, 3.3), fdi_anual_tipo(2016.0, 3.82), fdi_anual_tipo(2017.0, 2.38),
        fdi_anual_tipo(2018.0, 3.35), fdi_anual_tipo(2019.0, 3.15), fdi_anual_tipo(2020.0, 3.31),
        fdi_anual_tipo(2021.0, 5.44), fdi_anual_tipo(2022.0, 6.01)
        )
    );
COMMIT;

-- Países Bajos
INSERT INTO fdi_pais_objeto VALUES (
        'Países Bajos',
        'NLD',
        fdi_lista_tipo(
            fdi_anual_tipo(2000.0, 15.11), fdi_anual_tipo(2001.0, 12.02), fdi_anual_tipo(2002.0, 5.36),
        fdi_anual_tipo(2003.0, 3.51), fdi_anual_tipo(2004.0, 21.16), fdi_anual_tipo(2005.0, 30.5),
        fdi_anual_tipo(2006.0, 50.91), fdi_anual_tipo(2007.0, 85.98), fdi_anual_tipo(2008.0, 20.41),
        fdi_anual_tipo(2009.0, 23.12), fdi_anual_tipo(2010.0, 6.25), fdi_anual_tipo(2011.0, 38.81),
        fdi_anual_tipo(2012.0, 30.7), fdi_anual_tipo(2013.0, 35.13), fdi_anual_tipo(2014.0, 15.87),
        fdi_anual_tipo(2015.0, 48.5), fdi_anual_tipo(2016.0, 34.57), fdi_anual_tipo(2017.0, 23.52),
        fdi_anual_tipo(2018.0, -30.78), fdi_anual_tipo(2019.0, -13.67), fdi_anual_tipo(2020.0, -23.71),
        fdi_anual_tipo(2021.0, -10.95), fdi_anual_tipo(2022.0, 1.49)
        )
    );
COMMIT;

-- Bélgica
INSERT INTO fdi_pais_objeto VALUES (
        'Bélgica',
        'BEL',
        fdi_lista_tipo(
            fdi_anual_tipo(2000.0, 37.48), fdi_anual_tipo(2001.0, 37.26), fdi_anual_tipo(2002.0, 7.01),
        fdi_anual_tipo(2003.0, 10.86), fdi_anual_tipo(2004.0, 12.05), fdi_anual_tipo(2005.0, 8.73),
        fdi_anual_tipo(2006.0, 14.41), fdi_anual_tipo(2007.0, 20.5), fdi_anual_tipo(2008.0, 36.8),
        fdi_anual_tipo(2009.0, 15.95), fdi_anual_tipo(2010.0, 26.06), fdi_anual_tipo(2011.0, 31.04),
        fdi_anual_tipo(2012.0, 2.37), fdi_anual_tipo(2013.0, -5.66), fdi_anual_tipo(2014.0, -2.83), 
        fdi_anual_tipo(2015.0, -4.23), fdi_anual_tipo(2016.0, 12.13), fdi_anual_tipo(2017.0, -7.44),
        fdi_anual_tipo(2018.0, -7.67), fdi_anual_tipo(2019.0, -1.97), fdi_anual_tipo(2020.0, -5.74),
        fdi_anual_tipo(2021.0, 5.91), fdi_anual_tipo(2022.0, 2.0)
        )
    );
COMMIT;

-- Pórtugal
 INSERT INTO fdi_pais_objeto VALUES (
        'Portugal',
        'PRT',
        fdi_lista_tipo(
            fdi_anual_tipo(2000.0, 6.15), fdi_anual_tipo(2001.0, 5.03), fdi_anual_tipo(2002.0, 0.44),
        fdi_anual_tipo(2003.0, 6.27), fdi_anual_tipo(2004.0, 1.31), fdi_anual_tipo(2005.0, 1.71),
        fdi_anual_tipo(2006.0, 6.42), fdi_anual_tipo(2007.0, 2.5), fdi_anual_tipo(2008.0, 2.97),
        fdi_anual_tipo(2009.0, 2.35), fdi_anual_tipo(2010.0, 3.77), fdi_anual_tipo(2011.0, 4.24),
        fdi_anual_tipo(2012.0, 7.22), fdi_anual_tipo(2013.0, 6.44), fdi_anual_tipo(2014.0, 5.44),
        fdi_anual_tipo(2015.0, 0.64), fdi_anual_tipo(2016.0, 3.56), fdi_anual_tipo(2017.0, 5.02),
        fdi_anual_tipo(2018.0, 3.47), fdi_anual_tipo(2019.0, 4.5), fdi_anual_tipo(2020.0, 1.81),
        fdi_anual_tipo(2021.0, 3.61), fdi_anual_tipo(2022.0, 4.99)
        )
    );
COMMIT;

-- Grecia
INSERT INTO fdi_pais_objeto VALUES (
        'Grecia',
        'GRC',
        fdi_lista_tipo(
            fdi_anual_tipo(2000.0, -0.01), fdi_anual_tipo(2001.0, 0.0), fdi_anual_tipo(2002.0, 0.02),
        fdi_anual_tipo(2003.0, 0.72), fdi_anual_tipo(2004.0, 0.91), fdi_anual_tipo(2005.0, 0.28),
        fdi_anual_tipo(2006.0, 2.01), fdi_anual_tipo(2007.0, 0.62), fdi_anual_tipo(2008.0, 1.63),
        fdi_anual_tipo(2009.0, 0.85), fdi_anual_tipo(2010.0, 0.18), fdi_anual_tipo(2011.0, 0.39),
        fdi_anual_tipo(2012.0, 0.7), fdi_anual_tipo(2013.0, 1.25), fdi_anual_tipo(2014.0, 1.15),
        fdi_anual_tipo(2015.0, 0.65), fdi_anual_tipo(2016.0, 1.4), fdi_anual_tipo(2017.0, 1.72),
        fdi_anual_tipo(2018.0, 1.89), fdi_anual_tipo(2019.0, 2.41), fdi_anual_tipo(2020.0, 1.73),
        fdi_anual_tipo(2021.0, 2.81), fdi_anual_tipo(2022.0, 3.63)
        )
    );
COMMIT;

-- China
INSERT INTO fdi_pais_objeto VALUES (
        'China',
        'CHN',
        fdi_lista_tipo(
            fdi_anual_tipo(2000.0, 3.48), fdi_anual_tipo(2001.0, 3.51), fdi_anual_tipo(2002.0, 3.61),
        fdi_anual_tipo(2003.0, 3.49), fdi_anual_tipo(2004.0, 3.48), fdi_anual_tipo(2005.0, 4.55),
        fdi_anual_tipo(2006.0, 4.51), fdi_anual_tipo(2007.0, 4.4), fdi_anual_tipo(2008.0, 3.73),
        fdi_anual_tipo(2009.0, 2.57), fdi_anual_tipo(2010.0, 4.0), fdi_anual_tipo(2011.0, 3.71),
        fdi_anual_tipo(2012.0, 2.83), fdi_anual_tipo(2013.0, 3.04), fdi_anual_tipo(2014.0, 2.56),
        fdi_anual_tipo(2015.0, 2.19), fdi_anual_tipo(2016.0, 1.56), fdi_anual_tipo(2017.0, 1.35),
        fdi_anual_tipo(2018.0, 1.69), fdi_anual_tipo(2019.0, 1.31), fdi_anual_tipo(2015.0, 2.19),
        fdi_anual_tipo(2016.0, 1.56), fdi_anual_tipo(2017.0, 1.35), fdi_anual_tipo(2018.0, 1.69),
        fdi_anual_tipo(2015.0, 2.19), fdi_anual_tipo(2016.0, 1.56), fdi_anual_tipo(2017.0, 1.35),
        fdi_anual_tipo(2015.0, 2.19), fdi_anual_tipo(2016.0, 1.56), fdi_anual_tipo(2015.0, 2.19), 
        fdi_anual_tipo(2015.0, 2.19), fdi_anual_tipo(2015.0, 2.19), fdi_anual_tipo(2016.0, 1.56),
        fdi_anual_tipo(2017.0, 1.35), fdi_anual_tipo(2018.0, 1.69),  fdi_anual_tipo(2019.0, 1.31),
        fdi_anual_tipo(2020.0, 1.72), fdi_anual_tipo(2021.0, 1.93), fdi_anual_tipo(2022.0, 1.06)
        )
    );
COMMIT;

-- Consulta de análisis para identificar los 5 países con mayor promedio de FDI.
-- Utilizada para alimentar visualizaciones comparativas en Python/Power BI.

-- Top 5 mejores FDI
SELECT
    p.codigo_pais,
    p.nombre_pais,
    AVG(f.fdi_porcentaje) AS fdi_promedio
FROM
    fdi_pais_objeto p,
    TABLE(p.fdi_anual) f
GROUP BY
    p.codigo_pais,
    p.nombre_pais
ORDER BY
    fdi_promedio DESC
FETCH FIRST 6 ROWS ONLY;

-- Consulta de análisis para los 5 países con menor promedio de FDI.
-- Permite detectar regiones con menor atracción de inversión extranjera.

-- TOP 5 peores FDI
SELECT
    p.codigo_pais,
    p.nombre_pais,
    AVG(f.fdi_porcentaje) AS fdi_promedio
FROM
    fdi_pais_objeto p,
    TABLE(p.fdi_anual) f
WHERE
    p.codigo_pais != 'EUU'
GROUP BY
    p.codigo_pais,
    p.nombre_pais
ORDER BY
    fdi_promedio ASC
FETCH FIRST 5 ROWS ONLY;


-- Tabla que almacena los resultados generados por la simulación Monte Carlo
-- Cada fila representa un valor FDI simulado para un país, año y escenario.

CREATE TABLE simulaciones_montecarlo (
    id_simulacion NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pais VARCHAR2(10),
    año NUMBER,
    valor_simulado FLOAT,
    escenario_id NUMBER,
    fecha_generacion DATE DEFAULT SYSDATE
);

/*Tabla que registra alertas de riesgo detectadas automáticamente.
Se utiliza para almacenar casos donde el valor simulado está fuera de un rango 
lógico (por ejemplo, FDI negativo).*/

CREATE TABLE alertas_simulacion (
    id_alerta NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pais VARCHAR2(10),
    año NUMBER,
    valor_detectado FLOAT,
    fecha_alerta DATE DEFAULT SYSDATE
);


/*Trigger que se activa tras cada inserción en la tabla de simulaciones.
Si el valor simulado es menor a 0 o mayor a 10, se genera automáticamente 
una alerta en la tabla `alertas_simulacion*/

CREATE OR REPLACE TRIGGER trg_alerta_montecarlo
AFTER INSERT ON simulaciones_montecarlo
FOR EACH ROW
WHEN (NEW.valor_simulado < 0 OR NEW.valor_simulado > 10)
BEGIN
    INSERT INTO alertas_simulacion (
        pais, año, valor_detectado, fecha_alerta
    ) VALUES (
        :NEW.pais, :NEW.año, :NEW.valor_simulado, SYSDATE
    );
END;
/

-- Consults de prueba sobre tablas. 
SELECT * FROM simulaciones_montecarlo;
SELECT * FROM alertas_simulacion WHERE pais = 'CHN';

SELECT pais, COUNT(*) AS total_simulaciones
FROM simulaciones_montecarlo
GROUP BY pais
ORDER BY total_simulaciones DESC;

SELECT *
FROM alertas_simulacion
ORDER BY fecha_alerta DESC;

SELECT escenario_id, COUNT(*) 
FROM simulaciones_montecarlo 
WHERE pais = 'EUU' 
GROUP BY escenario_id 
ORDER BY escenario_id;
commit;


/*
Tabla que almacena información de empresas simuladas.
Incluye nombre, país, sector económico, ingresos base y su sensibilidad al FDI.
Esta información es la base para proyectar ingresos simulados bajo 
distintos escenarios.
*/

CREATE TABLE empresas_ficticias (
    id_empresa NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR2(50),
    pais VARCHAR2(5),
    sector VARCHAR2(30),
    ingresos_base FLOAT,
    sensibilidad_fdi FLOAT
);

/*Tabla que registra los ingresos simulados por empresa según distintos escenarios.
Cada fila representa un resultado de simulación vinculado a una empresa (id_empresa).
Incluye año, país, escenario simulado y la fecha en que se generó el dato.
*/

CREATE TABLE simulaciones_empresas (
    id_simulacion_empresa NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_empresa NUMBER,              -- FK a empresas_ficticias
    pais VARCHAR2(5),               -- Redundante, pero útil para filtrado rápido
    año NUMBER,
    escenario_id NUMBER,
    ingreso_simulado FLOAT,
    fecha_generacion DATE DEFAULT SYSDATE
);

-- Consultas de Prueba sobre tablas.
SELECT * FROM empresas_ficticias;
SELECT * FROM simulaciones_empresas;


/*
-- Tabla que almacena el Z-Score calculado para cada empresa en cada escenario
simulado.El Z-Score sirve como indicador de riesgo financiero, basado en el 
ingreso proyectado.
*/

CREATE TABLE zscore_empresas (
    id_zscore NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_empresa NUMBER,
    pais VARCHAR2(5),
    año NUMBER,
    escenario_id NUMBER,
    ingreso_simulado FLOAT,
    z_score FLOAT,
    fecha_generacion DATE DEFAULT SYSDATE
);
COMMIT;


/*
Tabla que almacena alertas generadas a partir de Z-Scores anómalos o críticos.
Incluye un mensaje descriptivo del riesgo detectado, junto con la empresa y 
el año.
*/

CREATE TABLE alertas_empresas (
    id_alerta NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_empresa NUMBER,
    año NUMBER,
    escenario_id NUMBER,
    z_score FLOAT,
    mensaje VARCHAR2(200),
    fecha_alerta DATE DEFAULT SYSDATE
);


/*
Trigger que detecta automáticamente valores críticos de Z-Score (< 1.8)
e inserta una alerta en la tabla `alertas_empresas`, indicando posible 
riesgo de quiebra.
*/

CREATE OR REPLACE TRIGGER trg_alerta_zscore
AFTER INSERT ON zscore_empresas
FOR EACH ROW
WHEN (NEW.z_score < 1.8)
BEGIN
    INSERT INTO alertas_empresas (
        id_empresa, año, escenario_id, z_score, mensaje
    ) VALUES (
        :NEW.id_empresa,
        :NEW.año,
        :NEW.escenario_id,
        :NEW.z_score,
        'Riesgo de quiebra detectado: Z-Score por debajo del umbral crítico'
    );
END;
/
commit;

-- Consultas de prueba sobre tablas.

SELECT * FROM zscore_empresas;
SELECT * FROM alertas_empresas;


SELECT
    f.anio AS AÑO,
    AVG(f.fdi_porcentaje) AS FDI_PROMEDIO
FROM
    fdi_pais_objeto p,
    TABLE(p.fdi_anual) f
WHERE
    p.codigo_pais = 'IRL'
GROUP BY
    f.anio
ORDER BY
    f.anio
;    

SELECT USER FROM dual;
SELECT table_name FROM user_tables;

SELECT COUNT(*) AS NUMERO
FROM alertas_empresas;
