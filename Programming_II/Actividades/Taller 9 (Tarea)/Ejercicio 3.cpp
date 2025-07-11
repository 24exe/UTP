/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

3. Suma de Elementos de un Vector
Problema: Dado un vector de enteros inicializado, escribe un programa que calcule y muestre la
suma de todos sus elementos.
Entrada: La primera línea contiene N, el Número de elementos del vector. La siguiente línea
contiene N enteros separados por espacio.
Salida: Un entero que representa la suma de los elementos del vector.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//PROTOTIPOS DE FUNCIÓNES AUX.
void data();

//FUN. DE PROCESO
void data(){
	cout<<"---SUMA DE ELEMENTOS DE UN VECTOR---\n\n";
	
	int elementos;
	int suma = 0;
	do{
		cout<<"Ingrese el número de elementos que tendra el vector: \n";
		cin>>elementos;
		cin.ignore();
		if(elementos < 1){
			cout<<"ERROR, deben ser mas de 0 elementos. \n";
		}
	}while(elementos < 1);
	
	vector<int> v;
	
	for(int i = 0; i < elementos; i++){
		int valor;
		cout<<"ingrese el elemento "<<i+1<<" del vector: \n";
		cin>>valor;
		v.push_back(valor);
		suma += v[i];
	}
	cout<<"La suma de los elementos del vector es: "<<suma<<endl;
	
}



//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
