/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

2. Añadiendo Elementos con push_back
Problema: Utiliza un vector vacío e implementa un bucle que utilice la función push_back para
añadir los Números del 1 al 5. Imprime el vector final.
Entrada: No aplicable.
Salida: Los Números del 1 al 5 en una sola línea, separados por espacios.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//PROTOTIPOS DE FUNCIÓNES AUX.
void data();

//FUN. DE PROCESO
void data(){
	cout<<"---AÑADIENDO ELEMENTOS CON PUSH_BACK---\n\n";
	vector<int> nums;
	//ciclo para llenar el contenedor vacío
	for(int i = 0; i < 5; i++){
		nums.push_back(i+1);
	} 
	//ciclo para mostrar el contenedor.
	for(size_t i = 0; i < nums.size(); i++){
		cout<<nums[i]<<" ";
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
