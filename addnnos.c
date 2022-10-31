#include<stdio.h>
int main()
{
    int i, n1, n2, sum=0;
    printf("Enter the value of n: ");
    scanf("%d", &n1);
    printf("Enter %d numbers: ", n1);
    for(i=0; i<n1; i++)
    {
        scanf("%d", &n2);
        sum = sum+n2;
    }
    printf("\nSum of all %d numbers = %d", n1, sum);
    return 0;
}