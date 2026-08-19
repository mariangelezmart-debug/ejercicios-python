#include <iostream>
#include <vector>
#include <string>

using namespace std;

// EJERCICIO 1: Determinar número primo (Básico)
bool esPrimo(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

// EJERCICIO 2: Promedio de notas en un vector (Intermedio)
double calcularPromedio(const vector<double>& notas) {
    double suma = 0;
    for (double nota : notas) {
        suma += nota;
    }
    return notas.empty() ? 0 : suma / notas.size();
}

// EJERCICIO 3: Estructura de Estudiante y búsqueda (Avanzado)
struct Estudiante {
    string nombre;
    int edad;
    double notaFinal;
};

int main() {
    // Prueba Ejercicio 1
    cout << "El 7 es primo?: " << (esPrimo(7) ? "Si" : "No") << endl;

    // Prueba Ejercicio 2
    vector<double> notas = {16.5, 18.0, 14.5, 19.0};
    cout << "Promedio: " << calcularPromedio(notas) << endl;

    // Prueba Ejercicio 3
    Estudiante est1 = {"Maria", 21, 18.5};
    cout << "Estudiante: " << est1.nombre << " | Nota: " << est1.notaFinal << endl;

    return 0;
}
