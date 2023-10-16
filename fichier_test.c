#include <stdio.h>

int main (void)
{
    int array[] = {30, 20, 50, 1, 2};
    int i;
    int len = sizeof(array) / sizeof(int);
    int bigger = 0;
    int sec_bigger = 0;

    for (i = 0; i < len; i++)
    {
        if (array[bigger] < array[i])
            {
                bigger = i;
            }
    }
    for (i = 0; i < len; i++)
    {
        if (i != bigger && array[sec_bigger] < array[i])
            {
                sec_bigger = i;
            }
    }
    printf ("%d", array[sec_bigger]);
    return 0;
}



