/* task2.c */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 16
int main() {
int i, j;
FILE *f;
char key[KEYSIZE];
int value1, value2;
value1 = 1523979529;
value2 = 1523986729;
f = fopen("./keys.txt", "w");
for (j = value1; j <= value2; j++) {
srand (j);
for (i = 0; i< KEYSIZE; i++) {
key[i] = rand()%256;
fprintf(f, "%.2x", (unsigned char)key[i]);
}
fprintf(f,"\n");
}
return 0;
}