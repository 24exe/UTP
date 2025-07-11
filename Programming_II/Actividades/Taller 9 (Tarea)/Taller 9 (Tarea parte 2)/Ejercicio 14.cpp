/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

14. Uso de clear para Vaciar un Vector
Problema: Crea un vector y a��dele algunos elementos. Utiliza el m�todo clear para vaciarlo
completamente y muestra el tama�o del vector despu�s de vaciarlo.

Entrada: La primera l�nea contiene N, el N�mero inicial de elementos del vector. La siguiente l�nea
contiene N enteros separados por espacio.
Salida: Un entero que representa el tama�o del vector despu�s de utilizar clear().
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
		cout<<"Ingrese el n�mero de elementos que tendra el vector: \n";
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
	cout<<"Tama�o del Vector "<<endl<<v.size()<<endl;
	
	v.clear(); //para vaciar vector. 
	cout<<"Vector Vacio: \n";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
	cout<<"Tama�o del Vector Vacio: "<<endl<<v.size()<<endl;

}




//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
