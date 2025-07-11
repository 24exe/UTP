/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

4. Duplicando Valores con el Operador []
Problema: Crea un vector de 5 elementos enteros. Utiliza un bucle para modificar cada elemento
del vector para que sea el doble de su índice. Imprime el vector resultante.
Entrada: No aplicable.
Salida: Los elementos del vector después de la modificación, separados por espacio.
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



//PROTOTIPOS DE FUNCIÓNES AUX.
void data();

//FUN. DE PROCESO
void data(){
	cout<<"---DUPLICANDO VALORES CON EL OPERADOR []---\n\n";
	
	vector<int>v={1,2,3,4,5};
	
	cout<<"Vector Original: \n";
	cout<<" V = { ";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<"} \n";
	
	//ciclo para duplicar vector
	for(size_t i = 0; i < v.size(); i++){
		v[i] =v[i]*2;
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
