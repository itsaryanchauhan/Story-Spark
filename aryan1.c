#include <stdio.h>
#include <string.h>

int main()
{
    int f (int *x, int c) 
    {
        c=c-1;
        if (c == 0) return 1;
        *x= *x + 1;
        return f(x,c) * (*x);
    }
    int p = 5;
    int answer = f(&p,p);
    printf("%d", answer);
}
