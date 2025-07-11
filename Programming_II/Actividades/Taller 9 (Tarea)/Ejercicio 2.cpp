/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

2. A�adiendo Elementos con push_back
Problema: Utiliza un vector vac�o e implementa un bucle que utilice la funci�n push_back para
a�adir los N�meros del 1 al 5. Imprime el vector final.
Entrada: No aplicable.
Salida: Los N�meros del 1 al 5 en una sola l�nea, separados por espacios.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//PROTOTIPOS DE FUNCI�NES AUX.
void data();

//FUN. DE PROCESO
void data(){
	cout<<"---A�ADIENDO ELEMENTOS CON PUSH_BACK---\n\n";
	vector<int> nums;
	//ciclo para llenar el contenedor vac�o
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
