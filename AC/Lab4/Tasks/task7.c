#include <stdio.h>
#include <openssl/bn.h>
#define NBITS 256

void printBN(char *msg, BIGNUM *a)
{
    /* Use BN_bn2hex(a) for hex string */
    /* Use BN_bn2dec(a) for decimal string*/
    char *number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}

int main()
{
    BN_CTX *ctx = BN_CTX_new();
    BIGNUM *s = BN_new();
    BIGNUM *n = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *message = BN_new();

    // Initialize p, q, e
    /* Insert the values of n and e from step 2 */
    /* Insert the value of s from step 3 */
    BN_hex2bn(&s,"");
    BN_hex2bn(&n, "");
    BN_hex2bn(&e, "");
    // signing : m^e mod n
    BN_mod_exp(message, s, e, n, ctx);
    printBN("encrypted Message = ", message);
    return 0;
}