#include <iostream>
#include <vector>

using namespace std;

template <class T>
void buble_sort(vector<T> &v )
{
	T temp;
	for (unsigned int i = 0; i < v.size() - 1; i++)
	{
		for (unsigned int j = 0; j < v.size() - i - 1; j++)
		{
			if (v[j] > v[j + 1])	//	Swap bigger values to the right. Biggest one is stored in the last cell.
			{
				swap(&v[j], &v[j + 1]);
			}
		}
	}
}

template <class T>
void insertion_sort(vector<T> &v)
{
	T temp;
	unsigned int j;		//	Needs to live even after for loops, so it is declared.
	for (unsigned int i = 1; i < v.size(); i++)
	{
		temp = v[i];	//	Save current element.
		for (j = i; j != 0 && v[j - 1] > temp; j--)		//	Pull bigger values.
		{
				v[j] = v[j - 1];
		}
		v[j] = temp;	//	Insert back element.
	}
}

template <class T>
void selection_sort(vector<T> &v)
{
	T temp;
	unsigned int local_min_index;
	for (unsigned int i = 0; i < v.size() - 1; i++)
	{
		local_min_index = i;	//	Assume the current element is the min value.
		for (unsigned int j = i + 1; j < v.size(); j++)
		{
			if (v[j] < v[local_min_index])	//	Find the min value of the rest.
			{
				local_min_index = j;
			}
		}
		swap(&v[i], &v[local_min_index]);	//	Swap min value with current cell.
	}
}

template <class T>
unsigned int partition_of_quick_sort(vector<T> &v, unsigned int low, unsigned int high)
{
	T temp;
	T pivot = v[low];
	unsigned int i = low + 1;
	unsigned int j = high;
	while (i < j)	//	Until we consume/traverse the entire array...
	{
		while (i < j && v[i] <= pivot)	{	i++;	}	//	Find next bigger element.
		while (i < j && v[j] >= pivot)	{	j--;	}	//	Find next smaller element.
		swap(&v[i], &v[j]);		//	Swap smaller with bigger value.
	}
	swap(&v[low], &v[j - 1]);	//	Last swap to place pivot.
	return j - 1;	//	Return the index of placed pivot.
}

template <class T>
void quick_sort(vector<T> &v, unsigned int low, unsigned int high)
{
	unsigned int pivot_index;
	while (low < high)	//	Until there is nothing else to sort...
	{
		pivot_index = partition_of_quick_sort(v, low, high);	//	Place pivot and get the index.
		quick_sort(v, low, pivot_index - 1);	//	Sort lower half.
		quick_sort(v, pivot_index + 1, high);	//	Sort higer half.
	}
}

template <class T>
vector<T> merge_of_merge_sort(vector<T> left, vector<T> right)
{
	unsigned int i = 0, j = 0, k = 0;
	vector<T> merged;
	while (i < left.size() && j < right.size())
	{
		if (left[i] < right[j])
		{
			merged[k++] = left[i++];
		}
		else
		{
			merged[k++] = right[j++];
		}
	}
	if (i != left.size())
	{
		while (i < left.size())
		{
			merged[k++] = left[i++];
		}
	}
	else
	{
		while (j < right.size())
		{
			merged[k++] = right[j++];
		}
	}

	left._Destroy();
	right._Destroy();
	return merged;
}

template <class T>
vector<T> merge_sort(vector<T> &v, unsigned int low, unsigned int high)
{
	unsigned int mid = (low + high) / 2;
	if (low < high)
	{
		vector<T> left = merge_sort(v, low, mid);
		vector<T> right = merge_sort(v, mid + 1, high);
		return merge_of_merge_sort(left, right);
	}
}

int main()
{
	//	Just functions, no main.
	system("pause");
	return 0;
}
