/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

5. Acceso Seguro con .at()
Problema: Repite el ejercicio anterior, pero utilizando el m�todo .at() para modificar los
elementos del vector. Aseg�rate de capturar y manejar cualquier excepci�n que pueda ocurrir.
Entrada: No aplicable.
Salida: Los elementos del vector despu�s de la modificaci�n, separados por espacio. Si se produce
una excepci�n, imprime "Excepci�n ocurrida";.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


/*
----------------------------------

NOTA: PUEDE QUE NO SE CORRIDO EN DEV-CPP, 
SE RECOMIENDA CORRER EN COMPILADOR EN LINEA.

LOS ERRORES QUE PODRIA MOSTRAR SON LOS SIGUIENTES.
[Error] in C++98 'v' must be initialized by constructor, not by '{...}'
[Error] could not convert '{1, 2, 3, 4, 5}' from '<brace-enclosed initializer list>' to 'std::vector<int>'

----------------------------------

*/



//PROTOTIPOS DE FUNCI�NES AUX.
void data();

//FUN. DE PROCESO
void data(){
	cout<<"---ACCESO SEGURO CON .AT()---\n\n";
	
	vector<int>v={1,2,3,4,5};
	
	cout<<"Vector Original: \n";
	cout<<" V = { ";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<"} \n";
	
	int elementos = v.size();
	
	//ciclo para duplicar vector
	for(int i = 0; i < elementos; i++){
		v.at(i) = v[i]*2;
		if(i > elementos or i < -1){
			cout<<"Excepci�n ocurrida \n";
		}
		
	}
	
	cout<<"Vector Duplicado: \n";
	cout<<" V = { ";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<"} \n";
}



//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
