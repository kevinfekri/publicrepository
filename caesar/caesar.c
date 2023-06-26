#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool only_digits(string key);
string rotate(string plaintext, int k);

int main(int argc, string argv[])
{
    string key = argv[1];

    if (argc != 2)
    {
        printf("Missing command-line argument.");
        return 1;
    }

    if (!only_digits(key))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int k = atoi(key);

    string plaintext = get_string("Enter a plaintext:  ");
    printf("Ciphertext: ");
    rotate(plaintext, k);
    printf("\n");
}

string rotate(string plaintext, int k)
{
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (islower(plaintext[i]))
        {
            plaintext[i] = plaintext[i] - 97;
            plaintext[i] = (plaintext[i] + k) % 26;
            plaintext[i] = plaintext[i] + 97;
        }
        else if (isupper(plaintext[i]))
        {
            plaintext[i] = plaintext[i] - 65;
            plaintext[i] = (plaintext[i] + k) % 26;
            plaintext[i] = plaintext[i] + 65;
        }
        printf("%c", plaintext[i]);
    }
    return 0;
}

bool only_digits(string key)
{
    for (int i = 0, n = strlen(key); i < n; i++)
    {
        if (!isdigit(key[i]))
        {
            return false;
        }
    }
    return true;
}
