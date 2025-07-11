/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Recursividad.

Taller en clase 7: Ejercicio 3.

*/

//BIBLIOTECAS
#include <iostream>


using namespace std;

//VAR. GLOBALES
int n;
int suma = 0;
//PROTOTIPOS DE FUNCIÓNES AUX.
void data();
int sumDigitos(int i);


//FUN. PARA PEDIR NUM.
void data(){
	cout<<"Digite el número del que quiere sumar sus digitos: ";
	cin>>n;
	while(n>1000000000 or n<0){
		cout<<"Error, ingrese un número que este entre 0 y 1000000000: ";
		cin>>n;
	}
}

//FUN. PARA SUMAR DIGITOS
int sumDigitos(int i){
	if(i<10){
		return i;
	}
	else{
		return i % 10 + sumDigitos(i/10);
	}
}



//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	cout<<"---SUMA DIGITOS DE UN NÚMERO (RECURSIVIDAD)---\n\n";
	data();
	
	int resultado = sumDigitos(n);
	cout<<"Suma de los digitos de "<<n<<": \n";
	cout<<resultado<<endl;
	system ("pause");
	return 0;
	
}
