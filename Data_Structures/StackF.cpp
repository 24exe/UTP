/*
============================
STACK [LIFO] (FINAL)
============================
Ejemplo Grafico:
    +----+
    | 50 |  <-- TOP
    +----+
    | 40 |
    +----+
    | 30 |
    +----+
    | 20 |
    +----+
    | 10 |
    +----+
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

};

template <typename T>
class Stack {
private:
    Vector<T> elements;


public:
//Constructor por defecto
    Stack(){
        Vector<T> elements;

    }


//Constructor con tamaño y número de elementos n.
    Stack(unsigned int size_, const T& value){
        //++i es mas eficiente
        for(unsigned int i = 0; i < size_; ++i){
            elements.push_back(value);
        }
        //Siempre se llama a Shrink to Fit como precaución.
        elements.shrink_to_fit();
    }


//Constructor que acepta una lista de inicialización
    Stack(std::initializer_list<T> list) : elements(list) {}

public:
    void push(const T& item) {
        elements.push_back(item);
    }

    void pop() {
        assert(!elements.empty());
            elements.pop_back();
    }

    const T& top() const {
        assert(!elements.empty());
        return elements.at(elements.size()-1);
    }

    bool empty() const {
        return elements.empty();
    }

    unsigned int size() const {
        return elements.size();
    }
//Solo para visualizar print.
    void print()const{
        int sizecopy = elements.size();
        cout << elements.at(sizecopy - 1) << "--> TOP" << endl; 
        for(int i = sizecopy - 1; i > 0; i--){
            cout << elements.at(i-1) << endl;
        }
        cout << endl;
    }
};

int main() {
    
    Stack<int> numbers = {1, 2, 2, 3, 4, 4, 5};
    cout << numbers.top() << endl;
    Stack<int> x(5, 10);
    cout << x.top() << endl;
    Stack<char> b;
    b.push('a');
    b.push('l');
    b.push('o');
    cout << b.top() << endl;
    b.push('h');
    b.print();
    cout << b.top() << endl;
    
    return 0;
}