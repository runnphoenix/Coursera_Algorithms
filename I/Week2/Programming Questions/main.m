//
//  main.m
//  QuickSort
//
//  Created by workMac on 15/11/2.
//  Copyright © 2015年 Gree. All rights reserved.
//

#import <Foundation/Foundation.h>

long count_first = 0;
long count_last = 0;
long count_median = 0;

int partition_first(int arr[],int lo,int hi)
{
    int pivot = arr[lo];
    int i = lo + 1;
    
    for (int j = i; j <= hi; j ++) {
        count_first ++;
        if (arr[j] < pivot) {
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i ++;
        }
    }
    
    arr[lo] = arr[i-1];
    arr[i-1]= pivot;
    
    return i-1;
}

int partition_last(int arr[],int lo,int hi)
{
    //调换第一个和最后一个元素的位置
    int temp = arr[lo];
    arr[lo] = arr[hi];
    arr[hi] = temp;
    
    //问题一的解法
    int pivot = arr[lo];
    int i = lo + 1;
    
    for (int j = i; j <= hi; j ++) {
        count_last ++;
        if (arr[j] < pivot) {
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i ++;
        }
    }
    
    arr[lo] = arr[i-1];
    arr[i-1]= pivot;
    
    return i-1;
}

int partition_median(int arr[],int lo,int hi)
{
    //获取中位数的index
    int index;
    int middle = arr[(hi-lo)/2+lo];
    int bigger = arr[lo] > middle ? arr[lo] : middle; int index_bigger = arr[lo] > middle ? lo : (hi-lo)/2+lo;
    int smaller = arr[lo] > middle ? middle : arr[lo];int index_smaller = arr[lo] > middle ? (hi-lo)/2+lo : lo;
    if (bigger < arr[hi]) {
        index = index_bigger;
    }else{
        if (smaller < arr[hi]) {
            index = hi;
        }else{
            index = index_smaller;
        }
    }
    //把中位数和第一个元素互换位置
    if (index != lo) {
        int temp = arr[lo];
        arr[lo] = arr[index];
        arr[index] = temp;
    }
    
    //问题一的解法
    int pivot = arr[lo];
    int i = lo + 1;
    
    for (int j = i; j <= hi; j ++) {
        count_median ++;
        if (arr[j] < pivot) {
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i ++;
        }
    }
    
    arr[lo] = arr[i-1];
    arr[i-1]= pivot;
    
    return i-1;
}

void quickSort_first (int arr[], int lo, int hi)
{
    if (lo >= hi) {
        return;
    }
    
    int p = partition_first(arr, lo, hi);
    quickSort_first(arr, lo, p-1);
    quickSort_first(arr, p+1, hi);
}

void quickSort_last (int arr[], int lo, int hi)
{
    if (lo >= hi) {
        return;
    }
    
    int p = partition_last (arr, lo, hi);
    quickSort_last(arr, lo, p-1);
    quickSort_last(arr, p+1, hi);
}

void quickSort_median (int arr[], int lo, int hi)
{
    if (lo >= hi) {
        return;
    }
    
    int p = partition_median (arr, lo, hi);
    quickSort_median(arr, lo, p-1);
    quickSort_median(arr, p+1, hi);
}

int main(int argc, const char * argv[]) {
    
    @autoreleasepool {
        //获取输入数组
        NSString *home = NSHomeDirectory();
        NSString *filePath = [home stringByAppendingPathComponent:@"/Desktop/QuickSort.txt"];
        NSString *fileContent = [NSString stringWithContentsOfFile:filePath encoding:NSUTF8StringEncoding error:nil];
        NSArray *numbers = [fileContent componentsSeparatedByString:@"\n"];
        int array[10000];
        for (int i = 0; i < 10000; i ++) {
            array[i] = [[numbers objectAtIndex:i]intValue];
        }
        
        //选取第一个元素为pivot
        int array_first[10000];
        for (int i = 0; i < 10000; i ++) {
            array_first[i] = array[i];
        }
        quickSort_first(array_first, 0, 9999);
        printf("count_first is %ld\n",count_first);
        
        //选取最后一个元素为pivot
        int array_last[10000];
        for (int i = 0; i < 10000; i ++) {
            array_last[i] = array[i];
        }
        quickSort_last(array_last, 0, 9999);
        printf("count_last is %ld\n",count_last);
        
        //选取中间数为pivot
        int array_median[10000];
        for (int i = 0; i < 10000; i ++) {
            array_median[i] = array[i];
        }
        quickSort_median(array_median, 0, 9999);
        printf("count_median is %ld\n",count_median);
    }
    
    return 0;
}
