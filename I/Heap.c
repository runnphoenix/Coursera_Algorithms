//
//  main.c
//  Heap
//
//  Created by Hanying Zhang on 16/6/20.
//  Copyright © 2016年 myself. All rights reserved.
//

#include <stdio.h>


void heapify(int array[], int n, int t) {
    int maxIndex = t;
    
    if (2*t <= n) {
        maxIndex = array[t] < array[2*t] ? 2*t : t;
    }
    if (2*t+1 <= n) {
        maxIndex = array[maxIndex] < array[2*t+1] ? 2*t+1 : maxIndex;
    }
    
    if (maxIndex != t) {
        int temp = array[t];
        array[t] = array[maxIndex];
        array[maxIndex] = temp;
        heapify(array, n, maxIndex);
    }
}

void buildHeap(int array[], int length) {
    for (int index = (length-1)/2; index > 0; index -= 1) {
        heapify(array, length, index);
    }
}

int getMax(int array[], int length)
{
    int result = array[1];
    array[1] = array[length-1];
    //delete last element
    length --;
    
    heapify(array, length, 1);
    
    return result;
}


int main(int argc, const char * argv[]) {
    int arr[] = {0, 1, 19, 23, 4, 7, 89, 37, 28, 62};
    buildHeap(arr, sizeof(arr)/sizeof(arr[0]));
    
    for (int i = 0; i < 10; i ++) {
        printf("%d ",arr[i]);
    }
    printf("\n");
    
    printf("max: %d\n",getMax(arr, sizeof(arr)/sizeof(arr[0])));
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i ++) {
        printf("%d ",arr[i]);
    }
    printf("\n");
    
    return 0;
}
