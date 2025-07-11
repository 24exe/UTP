//Factoriales

#include <iostream>

using namespace std;

//PROTOTIPOS DE FUNCIÓN
int factorial(int n);



//FUN. FACTORIAL
int factorial (int n){
	if(n == 0){
		return 1;
	}
	else{
		return n * factorial(n-1);
	}

}


//FUN. PRINCIPAL
int main (){
	setlocale(LC_ALL, "spanish");
	//para caracteres especiales en español, no es necesario añadir ninguna biblioteca.
	
	int num, f;
	cout<<"---FACTORIAL---\n\n";
	cout<<"Digite el número del que quiere el factorial: ";
	cin>>num;
	f = factorial(num);
	cout<<"El factorial del número ingresado es: "<<f<<".\n";
	
	system ("pause");
	return 0;
	
}
