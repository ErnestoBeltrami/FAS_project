#include <stdlib.h>

int main(){
  int a = 1;
  int b = 2; 
  int c = a + b; 

  int* p = malloc(sizeof(int));
  free(p);

  return 0;
}
