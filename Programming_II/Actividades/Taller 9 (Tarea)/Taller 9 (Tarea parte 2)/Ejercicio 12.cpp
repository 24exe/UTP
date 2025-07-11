/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

12. Crear un Vector a Partir de Otro
Problema: Inicializa un vector con los elementos de otro vector existente. Imprime ambos
vectores para mostrar que son iguales.

Entrada: La primera línea contiene N, el Número de elementos del vector original. La siguiente
línea contiene N enteros separados por espacio.
Salida: Dos líneas, cada una con los elementos de cada vector, separados por espacios,
demostrando que ambos vectores son iguales.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---CREAR UN VECTOR A PARTIR DE OTRO---\n\n";
	
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
	
	//inicializar vector a partir de otro.
	vector<int> u(v);
	
	//mostrar contenedores.
	cout<<"Vector Original: \n";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
	
	cout<<"Vector Copia: \n";
	for(size_t i = 0; i < u.size(); i++){
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
