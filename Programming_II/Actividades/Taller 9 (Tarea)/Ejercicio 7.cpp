/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

7. Observando size() y capacity()
Problema: Crea un vector y a�ade elementos del 1 al 10 uno a uno. Despu�s de cada adici�n,
imprime el size() y capacity() del vector para observar c�mo cambian.
Entrada: No aplicable.
Salida: Para cada elemento a�adido, imprime una l�nea con el size() y capacity() del vector,
separados por un espacio.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---OBSERVANDO SIZE() Y CAPACITY()---\n\n";
	
	cout<<"A�adiendo los elementos al vector: ";
	vector<int> v;
	//ciclo para rellenar contenedor
	for(int i = 0; i < 10; i++){
		int tam = v.size();
		int cap = v.capacity();
		int valor;
		cout<<"TAMA�O = "<<tam<<endl;
		cout<<"CAPACIDAD = "<<cap<<endl;
		cout<<"A�ade el elemento "<<i+1<<" al vector: ";
		cin>>valor;
		cin.ignore();
		v.push_back(valor);
	}
	cout<<"Elementos del Vector: \n";
	//ciclo para mostrar contenedor
	for(int i = 0; i < 10;  i++ ){
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
