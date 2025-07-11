/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

10. Revertir un Vector
Problema: Utiliza push_back y pop_back para crear un Nuevo vector que sea el inverso de un
vector dado. Imprime el vector resultante.

Entrada: La primera línea contiene N, el Número de elementos del vector. La siguiente línea
contiene N enteros separados por espacio.
Salida: Los elementos del vector invertido, separados por espacios.
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
	vector<int> u;
	
	for(int i = 0; i < elementos; i++){
		int valor;
		cout<<"ingrese el elemento "<<i+1<<" del vector: \n";
		cin>>valor;
		v.push_back(valor);
	}
	
	cout<<"Vector Original: \n";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
	//para invertir vector
	while (!v.empty()){
		u.push_back(v.back()); //llevar a la cola de u el primer elemento de v.
		v.pop_back(); //sacar el ultimo elemento de v.
	}
	
	
	cout<<"Vector Invertido: \n";
	for(size_t i = 0; i < u.size(); i++){
		cout<<u[i]<<" ";
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
