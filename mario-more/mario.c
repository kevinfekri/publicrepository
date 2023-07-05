#include <cs50.h>
#include <stdio.h>

int get_height(void);
void print_grid(int n);

int main(void)
{
    int n = get_height();
    print_grid(n);
}

int get_height(void)
{
    int n;
    do
    {
        n = get_int("Height :\n");
    }
    while (n < 1 || n > 8);
    return n;
}

void print_grid(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int k = n - 2; k >= i; k--)
        {
            printf(" ");
        }
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        int l;
        do
        {
            l = 1;
            l++;
            printf("  ");
        }
        while (l < 2);
        for (int m = 0; m <= i; m++)
        {
            printf("#");
        }
        printf("\n");
    }
}
