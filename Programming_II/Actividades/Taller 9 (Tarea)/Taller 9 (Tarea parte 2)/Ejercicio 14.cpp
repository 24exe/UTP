/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

14. Uso de clear para Vaciar un Vector
Problema: Crea un vector y añádele algunos elementos. Utiliza el método clear para vaciarlo
completamente y muestra el tamaño del vector después de vaciarlo.

Entrada: La primera línea contiene N, el Número inicial de elementos del vector. La siguiente línea
contiene N enteros separados por espacio.
Salida: Un entero que representa el tamaño del vector después de utilizar clear().
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>


using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---USO DE CLEAR PARA VACIAR UN VECTOR---\n\n";
	
	int elementos;
	do{
		cout<<"Ingrese el número de elementos que tendra el vector: \n";
		cin>>elementos;
		cin.ignore();
		if(elementos < 1){
			cout<<"ERROR, deben ser mas de 0 elementos. \n";
		}
	}while(elementos < 1);
	
	vector<float> v;
	
	//para rellenar contenedor v.
	for(int i = 0; i < elementos; i++){
		float valor;
		cout<<"ingrese el elemento "<<i+1<<" del vector: \n";
		cin>>valor;
		v.push_back(valor);
	}
	
	cout<<"Vector: \n";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
	cout<<"Tamaño del Vector "<<endl<<v.size()<<endl;
	
	v.clear(); //para vaciar vector. 
	cout<<"Vector Vacio: \n";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
	cout<<"Tamaño del Vector Vacio: "<<endl<<v.size()<<endl;

}




//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
