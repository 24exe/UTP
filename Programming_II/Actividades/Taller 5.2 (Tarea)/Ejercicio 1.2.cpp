/*
Programación II
Grupo: 5
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Arrays

Taller 6, Tarea: Ejercicio 1.
*/


//BIBLIOTECAS
#include <iostream>
#include <iomanip> //Para la precisión de los decimales.

using namespace std;


//FUN. PRINCIPAL
int main(){
    int numNotas, numMaterias;
    
    setlocale(LC_ALL, "spanish");
	//para caracteres especiales en español, no es necesario añadir ninguna biblioteca.
    
    
    cout<<"---Ejercicio 1: Cálculo del Promedio de Notas por Materia---\n\n";
    cout<<"Digite el número de materias: ";
    cin>>numMaterias;
    while(numMaterias < 0){
        cout<<"ERROR, digite un número positivo: ";
        cin>>numMaterias;
    }
    cout<<"Digite el número de notas por materia: ";
    cin>>numNotas;
     while(numNotas < 0){
        cout<<"ERROR, digite un número positivo: ";
        cin>>numNotas;
    }
    
    float materias[numMaterias][numNotas], promedio[numMaterias]; 
    float suma[1000]= {}; //se inicializa de esta manera para que no hayan valores indeterminados.
    
    
    //digitacion de notas
    for (int i = 0; i < numMaterias; i++){
        cout<<"Materia "<<i+1<<": \n";
        for(int j = 0; j < numNotas; j++){
            //cout<<"matrix ["<<i<<"]["<<j<<"]\n"; ---> para saber en que posición de la matriz esta el valor a ingresar.
            cout<<"Nota"<<j+1<<": ";
            cin>>materias[i][j];
            while (materias[i][j]<0 or materias[i][j] > 5){
		cout<<"ERROR, LAS NOTAS TIENEN QUE SER NÚMEROS POSITIVOS MENORES QUE 5.\n ";
		    cout<<"Digite la nota "<<j+1<<" nuevamente: ";
			cin>>materias[i][j];
			
            }
            suma[i] = suma[i]+materias[i][j]; //suma por fuera del bucle secundario para que no hayan problemas.
            
        }
    }
    
    for(int i = 0; i <numMaterias; i++){
        promedio[i] = suma[i]/numMaterias;
    }
    
    
    /*
    Ciclo usado para ver sumatoria de las notas.
    cout<<"suma de notas por materia: \n";
    for(int k = 0; k < numMaterias; k++){
        cout<<"Materia "<<k+1<<": ";
        cout<<suma[k]<<endl;
        
    }
    
    Ciclos alternativos que se pueden usar para mostrar el resultado.
    for(int i = 0; i <numMaterias; i++){
        promedio[i] = suma[i]/numMaterias;
    }
    
    cout<<"Promedio de notas por materia: \n";
    for(int k = 0; k < numMaterias; k++){
        cout<<"Materia "<<k+1<<": ";
        cout<<fixed<<setprecision(2)<<promedio[k]<<endl;
	    //fixed sirve para que el punto decimal no se mueva.	

    }
    */
    
    cout<<"Promedio de notas por materia: \n";
    for(int k = 0; k < numMaterias; k++){
        cout<<"Materia "<<k+1<<": ";
        cout<<fixed<<setprecision(2)<<suma[k]/numNotas<<endl;
        //fixed sirve para que el punto decimal no se mueva.
        
    }
    
    system("pause");
    return 0;
}
