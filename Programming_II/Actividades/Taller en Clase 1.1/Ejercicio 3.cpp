//Ejercicio 3 - Programacion II
// Nombre: Maycol Becerra, David Rivas, Carlos Eduardo Grisales
// Codigo: 1221714653, 1004685578, 1055750849
#include <iostream>
using namespace std;

int main (){

    int num1, num2, num3;
    cout << "Este es un programa que recibe tres numeros enteros y los ordena de menor a mayor." << endl;
    cout << "Ingrese el primer numero: " << endl;
    cin >> num1;
    cout << "Ingrese el segundo numero: " << endl;
    cin >> num2;
    cout << "Ingrese el tercer numero: " << endl;
    cin >> num3;
    cout << "Los numeros ordenados de menor a mayor son: " << endl;
    if (num1 < num2 && num1 < num3){
        if (num2 < num3){
            cout << num1 << ", " << num2 << ", " << num3 << endl;
        } else {
            cout << num1 << ", " << num3 << ", " << num2 << endl;
        }
    } else if (num2 < num1 && num2 < num3){
        if (num1 < num3){
            cout << num2 << ", " << num1 << ", " << num3 << endl;
        } else {
            cout << num2 << ", " << num3 << ", " << num1 << endl;
        }
    } else if (num3 < num1 && num3 < num2){
        if (num1 < num2){
            cout << num3 << ", " << num1 << ", " << num2 << endl;
        } else {
            cout << num3 << ", " << num2 << ", " << num1 << endl;
        }
    } else if (num1 == num2 && num1 == num3){
        if (num2 == num3){
            cout << "Los tres numeros son iguales" << endl;
        }
    }
    return 0;
}