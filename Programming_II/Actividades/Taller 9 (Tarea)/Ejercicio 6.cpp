/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

6. Impresión Utilizando size()
Problema: Escribe un programa que imprima los elementos de un vector, utilizando un bucle for
que se base en el tamaño del vector obtenido con el método .size().
Entrada: La primera línea contiene N, el Número de elementos del vector. La siguiente línea
contiene N enteros separados por espacio.
Salida: Los elementos del vector en una sola línea, separados por espacios.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---IMPRESIÓN UTILIZANDO SIZE()---\n\n";
	
	int elementos;
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
	}
	cout<<"Elementos del vector impresos con el metodo .size: ";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
}



//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
