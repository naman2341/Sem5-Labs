/* length_ext.c */
#include <stdio.h>
#include <arpa/inet.h>
#include <openssl/sha.h>
int main(int argc, const char *argv[])
{
  int i;
  unsigned char buffer[SHA256_DIGEST_LENGTH];
  SHA256_CTX c;
SHA256_Init(&c);
for(i=0; i<64; i++)
   SHA256_Update(&c, "*", 1);
// MAC of the original message M (padded)
c.h[0] = htole32(0x6f343800);
c.h[1] = htole32(0x1129a90c);
c.h[2] = htole32(0x5b163792);
c.h[3] = htole32(0x8bf38bf2);
c.h[4] = htole32(0x6e39e57c);
c.h[5] = htole32(0x6e951100);
c.h[6] = htole32(0x5682048b);
c.h[7] = htole32(0xedbef906);
// Append additional message
SHA256_Update(&c, "Extra message", 13);
SHA256_Final(buffer, &c);
for(i = 0; i < 32; i++) {
   printf("%02x", buffer[i]);
}
printf("\n");
return 0; }