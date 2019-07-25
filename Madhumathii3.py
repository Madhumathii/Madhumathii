#include <stdio.h>
int main()
{
    char chh;
    printf(" ");
    scanf("%c",&chh);
     if(chh=='a' || chh=='e' || chh=='i' || chh=='o' || chh=='u' || 
       chh=='A' || chh=='E' || chh=='I' || chh=='O' || chh=='U')
    {
        printf("'%c' is Vowel.", chh);
    }
    else if((chh >= 'a' && chh <= 'z') || (chh >= 'A' && chh <= 'Z'))
    {
        printf("'%c' is Consonant.", chh);
    }
    else 
    {
         printf("'%c' is not an alphabet.", chh);
    }

    return 0;
}
