/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

9. Eliminar el Último Elemento con pop_back
Problema: Crea un vector y añádele algunos elementos. Luego, elimina el último elemento usando
pop_back. Imprime el vector antes y después de la eliminación.
Entrada: La primera línea contiene N, el Número inicial de elementos del vector. La siguiente línea
contiene N enteros separados por espacio.
Salida: Primero, imprime el vector inicial en una línea. Después, imprime el vector después de
eliminar el último elemento en otra línea. Los elementos deben estar separados por espacios.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---ELIMINAR EL ÚLTIMO ELEMENTO CON POP_BACK---\n\n";
	
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
	
	cout<<"Vector: ";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
	
	//para eliminar el ultimo elemento del vector.
	v.pop_back();
	
	
	cout<<"Vector sin el ultimo elemento: ";
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
