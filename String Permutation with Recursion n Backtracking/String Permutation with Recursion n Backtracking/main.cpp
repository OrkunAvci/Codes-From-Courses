#include <iostream>
#include <string>

using namespace std;

string swap(string str, int index1, int index2)
{
	char temp = str[index1];
	str[index1] = str[index2];
	str[index2] = temp;
	return str;
}

void str_perm(string str, int depth = 0)
{
	//	str[depth];
	if (depth == str.size())
	{
		cout << str << endl;
		return;
	}

	str_perm(str, depth + 1);
	for (unsigned int i = depth + 1; i < str.size(); i++)
	{
		str = swap(str, depth, i);
		str_perm(str, depth + 1);
	}
}


int main()
{
	string str;
	cout << "Gime me a string = ";
	cin >> str;

	str_perm(str);	//	This is pass by value, nothing is changed.

	system("pause");
	return 0;
}
