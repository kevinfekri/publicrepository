#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string word = get_string("Write anything : \n");
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (word[i] >= 0 && word[i] <= 127)
        {
            int arr[8] = {0};
            int bit = 0;
            for (int j = 0; j < 8; j++)
            {
                arr[j] = word[i] % 2;
                word[i] = word[i] / 2;
            }
            for (int k = 7; k >= 0; k--)
            {
                bit = arr[k];
                print_bulb(bit);
            }
            printf("\n");
        }
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
