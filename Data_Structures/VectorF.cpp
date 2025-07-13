/*
============================
VECTOR (FINAL)
============================
Ejemplo Grafico:

        0x1234 
    |===================|
    |Storage:   0x7AB   |---------> dirección del primer elemento.
    |===================|
    |Capacity:  5       |---------> tiene capacidad para 5 elementos.
    |===================|
    |Size:      0       |---------> elemetos que tiene por dentro el vector.
    |===================|

*/


#include <iostream>
#include <cassert>

using namespace std;

template <typename T>
class Vector {

private: 
    T* storage_;
    unsigned int capacity_;
    unsigned int size_;

public:
//Constructor por defecto.
    Vector(){
        capacity_ = 5;
        storage_ = new T[capacity_];
        size_ = 0;
    }
//Constructor para vector de tamaño n.
    Vector(unsigned int c){
        capacity_ = c;
        storage_ = new T[capacity_];
        size_ = 0;
    }
//Constructor para vector de tamaño n y elementos.
    Vector(unsigned int c, T elem){
        capacity_ = c;
        storage_ = new T[capacity_];
        for (unsigned int i = 0; i < capacity_; i++){
            storage_[i] = elem;
        }
        size_ = capacity_;
    }
// Constructor que acepta una lista de inicialización
    Vector(initializer_list<T> list) {
        capacity_ = list.size();
        storage_ = new T[capacity_];
        size_ = 0;
        for (const T& elem : list) {
            storage_[size_++] = elem;
        }
    }

public:
//Metodo que retorna el tamaño del vector.
    unsigned int size() const {
    return size_;
    }
//Metodo que retorna la capacidad actual del vector.
    unsigned int capacity() const {
        return capacity_;
    }

    const T& at(unsigned int pos)const{
        assert(pos >= 0 && pos < size_);
        return storage_[pos];
    }
    const T& operator[](unsigned int index) const {
        return storage_ [index];
    }

private:

    void resize(){
        //cout << "Resize!" << endl;    //for debuginng
        unsigned int capacity2 = capacity_ * 1.5;
        T* storage2 = new T[capacity2];
        for(unsigned int i = 0; i < size_; i++){
            storage2[i] = storage_[i];
        }
        delete [] storage_;
        storage_ = storage2;
        capacity_ = capacity2;
    }
    //Metodo para descartar el exceso de capacidad
    void shrink_to_fit(){
        if(capacity_ > size_){
            //cout<<"Shrink to Fit!"<<endl; //for debuginng
            unsigned int capacity2 = size_;
            T* storage2 = new T[size_];
            for(unsigned int i = 0; i < size_+1; i++){
               storage2[i] = storage_[i];
            }
            delete [] storage_;
            storage_ = storage2;
            capacity_ = capacity2;
        }
    }


public:
//Metodo que inserta un elemento al final del vector.
    void push_back(const T& elem){
        if(size_ == capacity_){
            resize();
        }
        storage_[size_]= elem;
        size_++;
    }

//Metodo que elimina el ultimo elemento del vector.
    void pop_back(){
        size_--;
    }

//Metodo para insertar un elemento al principio del vector.
    void push_front(const T& elem) {
        if(size_ == capacity_){
            resize();
        }
        T* storage2 = new T[capacity_];
        storage2[0] = elem;
        for(unsigned int i = 1; i < size_+1; i++){
            storage2[i] = storage_[i-1];
        }
        delete [] storage_;
        storage_ = storage2;
        size_++;
    }
//Metodo para eliminar el primer elemento del vector.
    void pop_front(){
        T* storage2 = new T[capacity_];
        for(unsigned int i = 0; i < size_+1; i++){
            storage2[i] = storage_[i+1];
        }
        delete [] storage_;
        storage_ = storage2;
        size_--;
    }


//Metodo para insertar elementos en posiciones especificas
    void insert(unsigned int index, const T& elem){
        assert(index >= 0 && index <= size_);
        if(size_ == capacity_){
            resize();
        }
        
        T* storageAux = new T[size_];
        for (unsigned int i = 0; i < size_; i++){
            storageAux[i] = storage_[i];
        }

        for(unsigned int i = index; i < size_; i++){
            storage_[i+1] = storageAux[i]; 
        }
        storage_[index] = elem;
        size_++;
    }

//Metodo para borrar un elemento en una posicion especifica.
    void erase(unsigned int index){
        assert(index >= 0 && index <= size_);
        T* storageAux = new T[size_];
        for (unsigned int i = 0; i < size_; i++){
            storageAux[i] = storage_[i];
        }
        for(unsigned int j = index; j < size_; j++){
            storage_[j] = storageAux[j+1]; 
        }
        size_--;
    }


//Metodo que imprime el vector.
    void print()const{
        for(unsigned int i = 0; i < size_; i++){
            cout << " " << storage_[i];
        }
        cout << endl;
    }

//Metodo para saber si el vector esta vacio.
    bool empty() const {return size_ == 0;}

};


int main(){
    /*
    Vector<int> myVector;

    // Test push_back
    myVector.push_back(10);
    myVector.push_back(20);
    myVector.push_back(30);
    
    cout << myVector.size() << endl; // Expected: 3
    cout << myVector.capacity() << endl; // Expected: Initial capacity, e.g., 4 or 8
    
    // Test pop_back
    myVector.pop_back();
    cout << myVector.size() << endl; // Expected: 2
    
    // Test at with valid and invalid indices
    cout << myVector.at(0) << endl; // Expected: 10
    cout << myVector.at(1) << endl; // Expected: 20
    
    // Border case: Accessing an out-of-bounds index
    cout << myVector.at(2) << endl; // Should crash!
    
    // Border case: pop_back on empty vector
    Vector<int> emptyVector;
    emptyVector.pop_back(); // should crash!
    */

    return 0;
}