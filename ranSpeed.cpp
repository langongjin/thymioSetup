#include <iostream>
#include <fstream>
using namespace std;
int main() {
    ofstream fo;

    for(int i = 0; i < 100; i++)
    {
        fo.open("fo.txt",ios::trunc);
        fo << i << endl;
        fo.close();
        sleep(1);
        //cout << i << endl;
    }

    return 0;
}
