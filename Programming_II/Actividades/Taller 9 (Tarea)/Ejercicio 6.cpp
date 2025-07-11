/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

6. Impresi�n Utilizando size()
Problema: Escribe un programa que imprima los elementos de un vector, utilizando un bucle for
que se base en el tama�o del vector obtenido con el m�todo .size().
Entrada: La primera l�nea contiene N, el N�mero de elementos del vector. La siguiente l�nea
contiene N enteros separados por espacio.
Salida: Los elementos del vector en una sola l�nea, separados por espacios.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---IMPRESI�N UTILIZANDO SIZE()---\n\n";
	
	int elementos;
	do{
		cout<<"Ingrese el n�mero de elementos que tendra el vector: \n";
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
