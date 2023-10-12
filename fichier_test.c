#include <stdio.h>

void print_array(int array[], int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        printf("%d", array[i]);
    }
    printf("\n");
}

void reverse_array(int array[], int size)
{
    int deb = 0;
    int end = size -1;
    int temp;

    while (deb < end)
    {
        temp = array[deb];
        array[deb] = array[end];
        array[end] = temp;
        deb ++;
        end --;
    }
}

int main ()
{
    int array[] = {1, 2, 3, 4};
    int size = sizeof(array) / sizeof(array[0]);

    print_array(array, size);
    reverse_array(array, size);
    print_array(array, size);
    return 0;
}



