// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string word);

int main(int argc, string argv[1])
{
    if (argc != 2)
    {
        printf("Missing command-line argument.\n");
        return 1;
    }
    else
    {
	    printf("%s\n", replace(argv[1]));
        return 0;
    }
}

string replace(string word)
{
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        switch(word[i])
        {
            case (97) :
                printf("%c", word[i] - 43);
                break;
            case (101) :
                printf("%c", word[i] - 50);
                break;
            case (105) :
                printf("%c", word[i] - 56);
                break;
            case (111) :
                printf("%c", word[i] - 63);
                break;
            default :
                printf("%c", word[i]);
                break;
        }
    }
    printf("\n");
    return 0;
}
