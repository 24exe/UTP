//Factoriales

#include <iostream>

using namespace std;

//PROTOTIPOS DE FUNCI�N
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
	//para caracteres especiales en espa�ol, no es necesario a�adir ninguna biblioteca.
	
	int num, f;
	cout<<"---FACTORIAL---\n\n";
	cout<<"Digite el n�mero del que quiere el factorial: ";
	cin>>num;
	f = factorial(num);
	cout<<"El factorial del n�mero ingresado es: "<<f<<".\n";
	
	system ("pause");
	return 0;
	
}
