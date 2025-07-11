	/*
	Programación II
	Profesor: Felipe Gutiérrez Isaza
	Nombre: Carlos Eduardo Grisales Restrepo
	Codigo: 1055750849
	Tema: Vectores
	
	Taller 9 (Tarea).
	
	16. Intercalar Elementos con insert
	Problema: Dado un vector, utiliza insert para añadir un elemento dado en la tercera posición.
	Imprime el vector antes y después de la inserción.
	
	Entrada: La primera línea contiene N, el número de elementos del vector. La siguiente línea
	contiene N enteros separados por espacio. La tercera línea contiene el entero a insertar.
	Salida: Primero, imprime el vector original. Luego, imprime el vector después de la inserción.
	*/
	
	//BIBLIOTECAS
	#include <iostream>
	#include <vector>
	
	
	using namespace std;
	
	
	//FUN. DE PROCESO
	void data(){
		cout<<"---INTERCALAR ELEMENTOS CON INSERT---\n\n";
		int elementos;
		do{
			cout<<"Ingrese el número de elementos que tendra el vector: \n";
			cin>>elementos;
			cin.ignore();
			if(elementos < 1){
				cout<<"ERROR, deben ser mas de 0 elementos. \n";
			}
		}while(elementos < 1);
		
		vector<int> v;
		
		//para rellenar contenedor v.
		for(int i = 0; i < elementos; i++){
			int valor;
			cout<<"ingrese el elemento "<<i+1<<" del vector: \n";
			cin>>valor;
			v.push_back(valor);
		}
		vector<int> u(v);
		int insertado;
		cout<<"Ingrese el número que quiere insertar en la tercera posición del vector: \n";
		cin>>insertado;
		u.insert(u.begin() + 2, insertado);
		//mostrar contenedor.
		cout<<"Vector Original: \n";
		for(size_t i = 0; i < v.size(); i++){
			cout<<v[i]<<" ";
		}
        cout<<endl;
		cout<<"Vector con número insertado en la posicion 3: \n";
		for(size_t i = 0; i < u.size(); i++){
			cout<<u[i]<<" ";
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

