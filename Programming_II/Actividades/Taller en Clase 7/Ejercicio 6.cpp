/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Recursividad.

Taller en clase 7: Ejercicio 6.

*/

//BIBLIOTECAS
#include <iostream>


using namespace std;

//VAR. GLOBALES
int num;
int exponente;
int resultado;
//PROTOTIPOS DE FUNCIÓNES AUX.
void data();
int potencia();
int potenciaNegativa();


//FUN. AUX PARA PEDIR DATOS
void data(){
	cout<<"Digite el número del que quiere calcular la potencia: ";
	cin>>num;
	cout<<"¿A cuanto desea elevar el número? ";
	cin>>exponente;	
}

//FUN. RECURSIVA PARA EXPONENTES POSITIVOS
int potencia(int n, int exp){
	if(exp == 0){
		return 1;
	}
	else {
		return n * potencia(n, exp-1);
	}
}

//FUN. RECURSIVA PARA EXPONENTES NEGATIVOS
int potenciaNegativa(int n, int exp){
	if(exp == 0){
		return 1;
	}
	else {
		return n * potencia(n, exp+1);
	}
}




//FUN. PRINCIPAL
int main (){
	setlocale(LC_ALL, "spanish");
	cout<<"---CALCULAR LA POTENCIA DE UN NÚMERO (RECURSIVIDAD)---\n\n";
	data();
	if(exponente > 0){
		resultado = potencia(num, exponente);
		cout<<num<<"^"<<exponente<<" = "<<resultado<<endl;
	}
	else if(exponente == 0 and num < 0){
		cout<<num<<"^"<<exponente<<" = "<<-num / num<<endl;
	}
	else if(exponente == 0){
		cout<<num<<"^"<<exponente<<" = "<<num / num<<endl;
	}
	else{
		resultado = potencia(num, exponente * -1);
		cout<<num<<"^"<<exponente<<" = "<<"1/"<<resultado<<endl;
	}
	
	system ("pause");
	return 0;
}

