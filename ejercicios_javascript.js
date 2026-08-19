// ==========================================
// EJERCICIO 1: Validar correo electrónico (Básico)
// ==========================================
function validarEmail(email) {
    return email.includes("@") && email.includes(".");
}
console.log("¿Email válido?:", validarEmail("maria@example.com"));

// ==========================================
// EJERCICIO 2: Filtrar números pares y multiplicar (Intermedio)
// ==========================================
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const paresMultiplicados = numeros
    .filter(num => num % 2 === 0)
    .map(num => num * 2);

console.log("Pares duplicados:", paresMultiplicados);

// ==========================================
// EJERCICIO 3: Consumo de API asíncrona Async/Await (Avanzado)
// ==========================================
async function obtenerDatos() {
    try {
        const respuesta = await fetch('https://jsonplaceholder.typicode.com/todos/1');
        const datos = await respuesta.json();
        console.log("Tarea obtenida:", datos);
    } catch (error) {
        console.error("Error al obtener datos:", error);
    }
}
obtenerDatos();
