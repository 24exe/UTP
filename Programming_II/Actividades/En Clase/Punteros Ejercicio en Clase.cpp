/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Punteros.

Taller 10 en Clase.

SUMAR DOS N�MEROS A TRAVES DE PUNTEROS
*/


using namespace std; 


#include <iostream>

int main(){
	setlocale(LC_ALL, "spanish");
    int a, b;
    int *p1, *p2;
    
    cout<<"Digite el n�mero 1: ";
    cin>>a;
    p1 = &a;
    cout<<"Digite el n�mero 2: ";
    cin>>b;
    p2 = &b;
    
    cout<<"La suma de los dos n�meros es: "<<*p1 + *p2<<endl;
    
    system("pause");
    return 0;
}

