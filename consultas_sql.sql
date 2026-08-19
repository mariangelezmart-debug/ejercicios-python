-- ==========================================
-- CREACIÓN DE TABLAS Y CONSULTAS SQL
-- ==========================================

-- 1. Crear tabla de estudiantes
CREATE TABLE estudiantes (
    id_estudiante INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    carrera VARCHAR(50),
    promedio DECIMAL(4,2)
);

-- 2. Insertar registros de prueba
INSERT INTO estudiantes (nombre, carrera, promedio) VALUES
('Maria Gonzalez', 'Informatica', 18.5),
('Carlos Perez', 'Informatica', 15.0),
('Ana Gomez', 'Industrial', 16.8);

-- 3. Consultas SQL
-- Obtener estudiantes de Informática con promedio mayor o igual a 16
SELECT nombre, carrera, promedio 
FROM estudiantes 
WHERE carrera = 'Informatica' AND promedio >= 16.0
ORDER BY promedio DESC;
