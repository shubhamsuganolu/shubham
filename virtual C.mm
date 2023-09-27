#include<iostream>
using namespace std;

class A {
public:
    int a;
    A()// construtor 
    {
           a=10;
    }
};
class B:public virtual A {
};
class C:public virtual A {
};
class D:public virtual A { 
};

int main()
{
    D object;// object creation of class d
    cout<<"a="<<object.a<<endl;

    return 0;
}