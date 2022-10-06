#include <iostream>
#include <vector>
#include "src/scalarAdd.h"

using namespace::std;

int scalarAdd(vector<int> my_vector)
{
  int my_sum = 0;
  for (auto iv = my_vector.begin(); iv != my_vector.end(); iv++)       
      my_sum += *iv;

  return my_sum;
}