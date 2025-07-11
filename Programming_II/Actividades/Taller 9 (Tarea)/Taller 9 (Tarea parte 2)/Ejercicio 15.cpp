/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

15. Cambiar el Tamaño de un Vector con resize
Problema: Crea un vector y modifica su tamaño con resize. Imprime su tamaño y capacidad antes
y después de la modificación para observar los cambios.

Entrada: La primera línea contiene N, el número inicial de elementos del vector. La segunda línea
contiene los N enteros iniciales del vector. La tercera línea contiene un entero M que será el nuevo
tamaño del vector.
Salida: Dos líneas, cada una mostrando el tamaño y la capacidad del vector antes y después de
usar resize, respectivamente.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>


using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---CAMBIAR EL TAMAÑO DE UN VECTOR CON RESIZE---\n\n";
	
	int elementos;
	int elementos2;
	
	do{
		cout<<"Ingrese el número de elementos que tendra el vector: \n";
		cin>>elementos;
		cin.ignore();
		if(elementos < 1){
			cout<<"ERROR, deben ser mas de 0 elementos. \n";
		}
	}while(elementos < 1);
	
	vector<int> v(elementos);
	const int tam = v.size();
	const int cap = v.capacity();
	
	
	//cambiar el tamaño del vector
	do{
		cout<<"Ingrese el cambio de tamaño del vector: \n";
		cin>>elementos2;
		cin.ignore();
		if(elementos2 < 1){
			cout<<"ERROR, deben ser mas de 0 elementos. \n";
		}
	}while(elementos2 < 1);
	v.clear();
	v.resize(elementos2);
	const int tam2 = v.size();
	const int cap2 = v.capacity();

	cout<<endl;
	cout<<"Tamaño del Vector Original: "<<tam<<endl;
	cout<<"Capacidad del Vector Original: "<<cap<<endl;
	cout<<"Tamaño del Vector con Cambio de Tamaño: "<<tam2<<endl;
	cout<<"Capacidad del Vector con Cambio de Tamaño: "<<cap2<<endl;

	cout<<endl;


}




//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
