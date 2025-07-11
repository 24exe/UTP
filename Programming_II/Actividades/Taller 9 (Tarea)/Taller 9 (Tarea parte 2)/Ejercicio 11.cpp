/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

11. Uso de front y back
Problema: Dado un vector de enteros, imprime el primer y último elemento del vector utilizando
los métodos front() y back().

Entrada: La primera línea contiene N, el Número de elementos del vector. La siguiente línea
contiene N enteros separados por espacio.
Salida: Dos enteros en una línea, el primer y último elemento del vector, separados por un
espacio.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---USO DE FRONT Y BACK---\n\n";
	
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
	
	//para rellenar contenedor v.
	for(int i = 0; i < elementos; i++){
		int valor;
		cout<<"ingrese el elemento "<<i+1<<" del vector: \n";
		cin>>valor;
		v.push_back(valor);
	}
	
	cout<<"Vector: \n";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
	
	//primer elemento
	cout<<"Primer elemento del Vector: "<< v.front()<<endl;
	//ultimo elemento
	cout<<"Ultimo elemento del Vector: "<< v.back()<<endl;
	cout<<endl;
}




//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
