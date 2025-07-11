/*
ProgramaciÃ³n II
Profesor: Felipe GutiÃ©rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

13. Calcula la Media de los Elementos de un Vector
Problema: Dado un vector de enteros, calcula y muestra la media de sus elementos.

Entrada: La primera línea contiene N, el Número de elementos del vector. La siguiente línea
contiene N enteros separados por espacio.
Salida: Un Número flotante que representa la media de los elementos del vector, redondeado a
dos decimales.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>
#include <iomanip> //necesario para setprecision y fixed


using namespace std;


//FUN. DE PROCESO
void data(){
	cout<<"---CALCULA LA MEDIA DE LOS ELEMENTOS DE UN VECTOR---\n\n";
	
	int elementos;
	float suma;
	float promedio;
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
		suma += v[i];
	}
	
	promedio = suma/elementos;
	//mostrar contenedores.
	cout<<"Vector: \n";
	for(size_t i = 0; i < v.size(); i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
	cout<<"El promedio de los elementos del Vector es: "<<fixed<<setprecision(2)<<promedio<<endl;
	cout<<endl;

}




//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}
