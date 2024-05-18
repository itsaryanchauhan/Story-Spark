#include<stdio.h>
void swap (int a, int b) {
int temp;
temp = a;
a = b;
b = temp;
printf("After swapping 1st number is %d and 2nd number is %d", a,b);
}
int main(void) {
int first, second;
scanf("%d %d", &first, &second);
swap(first, second);
printf("\n After swap function called 1st number is %d and 2nd number is %d", first, second);
return 0;
}