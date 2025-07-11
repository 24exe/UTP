/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

8. Buscar el M�ximo Elemento
Problema: Dado un vector de enteros, escribe un programa que encuentre y muestre el valor
m�ximo dentro del vector.
Entrada: La primera l�nea contiene N, el N�mero de elementos del vector. La siguiente l�nea
contiene N enteros separados por espacio.
Salida: Un entero que representa el valor m�ximo encontrado en el vector.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---BUSCAR EL M�XIMO ELEMENTO---\n\n";
	
	int elementos;
	int maximo = 0;
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
		if(valor>maximo){
			maximo = valor;
		}
		v.push_back(valor);
	}
	cout<<"Elementos del Vector: ";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
	cout<<"Elemento M�ximo del Vector: "<<maximo<<endl;
}




//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
