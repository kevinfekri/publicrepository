#include <cs50.h>
#include <stdio.h>

int length(long number);
bool checksum(long number);
bool valid(long number);

int main(void)
{
    long number = get_long("Write a credit card number : \n");
    length(number);
    checksum(number);
    valid(number);
}

int length(long number)
{
    long n = number;
    int count = 0;
    for (long i = n; 0 < i; i = i / 10)
    {
        count = count + 1;
    }
    return count;
}

bool checksum(long number)
{
    long sum = 0;
    long n_1 = 0;
    long sum_2 = 0;
    long n_2 = 0;
    for (int i = 0, n = length(number); (i * 2) < n; i++)
    {
        n_1 = number % 10;
        sum += n_1;
        n_1 = 0;
        number = number / 10;

        n_2 = number % 10;
        n_2 = n_2 * 2;

        int modulo = 0;
        int divide = 0;
        if (n_2 > 9)
        {
            modulo = n_2 % 10;
            divide = n_2 / 10;
            n_2 = modulo + divide;
        }

        sum_2 += n_2;
        n_2 = 0;
        number = number / 10;
    }

    if ((sum + sum_2) % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool valid(long number)
{
    long i16 = 1000000000000000;
    long i15 = 100000000000000;
    long i14 = 10000000000000;
    long i13 = 1000000000000;

    if (checksum(number) == true)
    {
        if (length(number) == 15 && ((number / i14 == 34) || (number / i14 == 37)))
        {
            printf("AMEX\n");
        }
        else if (length(number) == 16 && ((number / i15 == 51) || (number / i15 == 52) || (number / i15 == 53)))
        {
            printf("MASTERCARD\n");
        }
        else if (length(number) == 16 && ((number / i15 == 54) || (number / i15 == 55)))
        {
            printf("MASTERCARD\n");
        }
        else if ((length(number) == 13 && number / i13 == 4) || (length(number) == 16 && number / i16 == 4))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
        return 0;
    }
    else
    {
        printf("INVALID\n");
    }
    return 0;
}
