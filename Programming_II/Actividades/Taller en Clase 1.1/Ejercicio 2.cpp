/*
Programación II
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Nombre: David Rivas
Codigo: 1004685578
Nombre:	Maycol Becerra
Codigo: 1221714653
Tema: Funciones Secuenciales.


Taller en clase 1: Ejercicio 2.
*/
#include<iostream>
using namespace std;

int main(){
	int edad;
	setlocale(LC_ALL, "Spanish"); //Se usa para caracteres especiales, en este caso la "ñ" 
	
	cout<<"\tEste programa lo clasifica segun su edad"<<endl<<endl;
	cout<<"Ingrese su edad: ",cin>>edad;
	
	if((edad > 0)&&(edad <= 11)){
		cout<<"Niño"<<endl;
	}
	else if((edad > 11)&&(edad <= 18)){
		cout<<"Adolescente "<<endl;
	}
	else if((edad > 18)&&(edad <= 100)){
		cout<<"Adulto "<<endl;
	}
	else{
		cout<<"Edad incorrecta"<<endl;
	}
	
	return 0;
}
