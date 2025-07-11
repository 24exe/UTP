#include <iostream>

using namespace std;


int sumavector(int vector[100],int i){
	int sumaElementos = vector[i];
	if(i < 0){
		return 0;
	}	
	else{
		sumaElementos += sumavector(vector, i-1);
	}
	return sumaElementos;
	
	
}

int main(){
	setlocale(LC_ALL, "spanish");
	
	cout<<"Número de elementos del vector: ";
	int n;
	cin>>n;
	int vector[n];
	int suma;
	
	for(int i = 0; i < n; i++){
		cout<<"Vector["<<i<<"]: ";
		cin>>vector[i];
	}
	
	
	suma = sumavector(vector, n-1);
	cout <<"Suma de elementos del vector: "<<suma<<endl;
	
	system ("pause");
	return 0;
	
}
