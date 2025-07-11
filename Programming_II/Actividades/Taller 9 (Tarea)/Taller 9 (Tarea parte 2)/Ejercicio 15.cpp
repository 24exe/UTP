/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

15. Cambiar el Tama�o de un Vector con resize
Problema: Crea un vector y modifica su tama�o con resize. Imprime su tama�o y capacidad antes
y despu�s de la modificaci�n para observar los cambios.

Entrada: La primera l�nea contiene N, el n�mero inicial de elementos del vector. La segunda l�nea
contiene los N enteros iniciales del vector. La tercera l�nea contiene un entero M que ser� el nuevo
tama�o del vector.
Salida: Dos l�neas, cada una mostrando el tama�o y la capacidad del vector antes y despu�s de
usar resize, respectivamente.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>


using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---CAMBIAR EL TAMA�O DE UN VECTOR CON RESIZE---\n\n";
	
	int elementos;
	int elementos2;
	
	do{
		cout<<"Ingrese el n�mero de elementos que tendra el vector: \n";
		cin>>elementos;
		cin.ignore();
		if(elementos < 1){
			cout<<"ERROR, deben ser mas de 0 elementos. \n";
		}
	}while(elementos < 1);
	
	vector<int> v(elementos);
	const int tam = v.size();
	const int cap = v.capacity();
	
	
	//cambiar el tama�o del vector
	do{
		cout<<"Ingrese el cambio de tama�o del vector: \n";
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
	cout<<"Tama�o del Vector Original: "<<tam<<endl;
	cout<<"Capacidad del Vector Original: "<<cap<<endl;
	cout<<"Tama�o del Vector con Cambio de Tama�o: "<<tam2<<endl;
	cout<<"Capacidad del Vector con Cambio de Tama�o: "<<cap2<<endl;

	cout<<endl;


}




//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
