/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Punteros.

Taller 10 en Clase.

SUMAR DOS NÚMEROS A TRAVES DE PUNTEROS
*/


using namespace std; 


#include <iostream>

int main(){
	setlocale(LC_ALL, "spanish");
    int a, b;
    int *p1, *p2;
    
    cout<<"Digite el número 1: ";
    cin>>a;
    p1 = &a;
    cout<<"Digite el número 2: ";
    cin>>b;
    p2 = &b;
    
    cout<<"La suma de los dos números es: "<<*p1 + *p2<<endl;
    
    system("pause");
    return 0;
}

