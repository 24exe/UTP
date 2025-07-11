/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

17. Eliminar un Elemento Específico con erase
Problema: Crea un vector y utiliza erase para eliminar el tercer elemento. Imprime el vector antes
y después de la eliminación.

Entrada: La primera línea contiene N, el número de elementos del vector. La siguiente línea
contiene N enteros separados por espacio.
Salida: Primero, imprime el vector original. Luego, imprime el vector después de eliminar el tercer
elemento.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>


using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---ELIMINAR UN ELEMENTO ESPECÍFICO CON ERASE---\n\n";
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
	vector<int> u(v);

	u.erase(u.begin() + 2);
	//mostrar contenedor.
	cout<<"Vector Original: \n";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
       cout<<endl;
	cout<<"Vector con número eliminado en la posicion 3: \n";
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
