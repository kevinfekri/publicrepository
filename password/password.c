// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    int j = 0;
    int k = 0;
    int l = 0;
    int m = 0;
    for (int i = 0, n = strlen(password); i < n; i++)
    {
        if (islower(password[i]))
        {
            j++;
        }
        else if (isupper(password[i]))
        {
            k++;
        }
        else if (isdigit(password[i]))
        {
            l++;
        }
        else if ((password[i] > 32 && password[i] < 48) || (password[i] > 57 && password[i] < 65))
        {
            m++;
        }
        else if ((password[i] > 90 && password[i] < 97) || (password[i] > 122 && password[i] < 127))
        {
            m++;
        }
    }

    if ((j > 0) && (k > 0) && (l > 0) && (m > 0))
    {
        return true;
    }
    else
    {
        return false;
    }
}
