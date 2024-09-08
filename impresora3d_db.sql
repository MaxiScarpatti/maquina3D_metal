USE impresora_3d_metal;

CREATE TABLE impresora_3d_metal (
    id SERIAL PRIMARY KEY,
    temperatura INT CHECK (temperatura BETWEEN 0 AND 1500),
    velocidad_impresion INT CHECK (velocidad_impresion BETWEEN 1 AND 10),
    nivel_polvo_metal DECIMAL(5, 2) CHECK (nivel_polvo_metal BETWEEN 0 AND 100),
    modelo VARCHAR(100) NOT NULL
);

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (200, 5, 85.00, 'Model X1');

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (300, 7, 90.50, 'Model X2');

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (1000, 10, 45.00, 'Model Pro M2');

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (800, 6, 60.00, 'Model Z3');

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (0, 3, 100.00, 'Model A1');

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (1500, 10, 10.00, 'Model X3 Max');

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (750, 4, 70.00, 'Model S5');

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (500, 8, 50.00, 'Model Z5');

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (1200, 9, 20.00, 'Model V2');

INSERT INTO impresora_3d_metal (temperatura, velocidad_impresion, nivel_polvo_metal, modelo) 
VALUES (250, 2, 95.00, 'Model R1');

SELECT * FROM impresora_3d_metal;

SELECT modelo, temperatura
FROM impresora_3d_metal
WHERE temperatura > 1000;

SELECT modelo, nivel_polvo_metal
FROM impresora_3d_metal
WHERE nivel_polvo_metal < 50;

SELECT modelo, velocidad_impresion
FROM impresora_3d_metal
ORDER BY velocidad_impresion DESC;

SELECT modelo, nivel_polvo_metal
FROM impresora_3d_metal
WHERE nivel_polvo_metal BETWEEN 50 AND 100;