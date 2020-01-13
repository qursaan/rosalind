#include <algorithm>
#include <iostream>
#include <vector>
#include <fstream>

using std::vector;

int get_majority_element(vector<int> &a, int left, int right) {
  if (left == right) return -1;
  if (left + 1 == right) return a[left];

  sort(a.begin(),a.end());
  int mid = (left+right)/2;
  while( left+mid < right ){
    if(a[left]==a[left+mid])
      return a[left];
    left++;
  }
  return -1;
}

int main() {
  int n , m;

  std::ofstream writer("output_maj.txt");
  std::ifstream reader("rosalind_maj.txt");
  if (!reader.is_open()){
    std::cout<< "FILE NOT FOUND\n";
    return -1;
  }

  reader >> m >> n;
  vector<int> a(n);
  std::cout<< "n "<< n << " m "<< m << std::endl;
  for (size_t j = 0; j < m; ++j) {
    for (size_t i = 0; i < n; ++i) {
      reader >> a[i];
    }
    writer << get_majority_element(a, 0, n) << " ";
  }
  std::cout<< "FINISHED "<< std::endl;
  reader.close();
  writer.close();
  return 0;
}
