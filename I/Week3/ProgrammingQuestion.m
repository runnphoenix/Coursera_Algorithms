//
//  main.m
//  week3
//
//  Created by workMac on 15/11/6.
//  Copyright © 2015年 Gree. All rights reserved.
//

#import <Foundation/Foundation.h>

#define VCOUNT 200

NSMutableArray* getGraphList()
{
    NSString *home = NSHomeDirectory();
    NSString *filePath = [home stringByAppendingPathComponent:@"/Desktop/kargerMinCut.txt"];
    NSString *fileContent = [NSString stringWithContentsOfFile:filePath encoding:NSUTF8StringEncoding error:nil];
    NSArray *numbers = [fileContent componentsSeparatedByString:@"\n"];
    
    NSMutableArray *graph = [NSMutableArray array];
    
    for (NSUInteger i = 0; i < VCOUNT; i ++) {
        NSString *rowString = numbers[i];
        NSMutableArray *rowNumbers = [NSMutableArray arrayWithArray:[rowString componentsSeparatedByString:@"\t"]];
        [rowNumbers removeLastObject];
        [graph addObject:rowNumbers];
    }
    return graph;
}

NSUInteger contraction(NSMutableArray *gra)
{
    //1. 随机获取一条边
    //1.1 第一个点
    NSUInteger firstVIndex = arc4random() % (gra.count - 1);
    NSUInteger firstV = [[[gra objectAtIndex:firstVIndex]firstObject]integerValue];
    //1.2 第二个点
    NSMutableArray *firstRow = [gra objectAtIndex:firstVIndex];
    NSUInteger secondV;
    if (firstRow.count > 2) {
        secondV = [[firstRow objectAtIndex: (arc4random() % (firstRow.count - 2) + 1)]integerValue];
    }else{
        return firstRow.count - 1;
    }
    //找到第二个点现在处于第几行
    NSUInteger secondVIndex = 0;
    NSArray *secondRow;
    for (NSUInteger i = 0; i < gra.count; i ++) {
        NSArray *row = gra[i];
        if (secondV == [row[0]integerValue]) {
            secondVIndex = i;
            secondRow = row;
        }
    }
    
    //2. 合并这条边
    //2.1 把所有的数据值中的secondV替换为firstV
    for (NSMutableArray *array in gra) {
        for (NSUInteger i = 1;i < array.count; i ++) {
            if ([array[i]integerValue] == secondV) {
                array[i] = @(firstV);
            }
        }
    }
    
    //2.2 把secondRow中的所有值添加到firstRow中，删除secondRow
    for (NSUInteger i = 1; i < secondRow.count; i ++) {
        [firstRow addObject:secondRow[i]];
    }
    [gra removeObjectAtIndex:secondVIndex];
    
    //2.3 firstRow中的所有firstV删除
    NSMutableArray *toDelete = [NSMutableArray array];
    for (NSUInteger i = 1; i < firstRow.count; i ++) {
        if ([firstRow[i] integerValue] == firstV) {
            [toDelete addObject:@(i)];
        }
    }
    NSMutableIndexSet *indexS = [[NSMutableIndexSet alloc]init];
    for (NSUInteger i = 0; i < toDelete.count; i ++) {
        [indexS addIndex:[toDelete[i]integerValue]];
    }
    [firstRow removeObjectsAtIndexes:indexS];
    
    //返回被删除的顶点
    return secondV;
}

NSUInteger getMinCut(NSMutableArray *graphic)
{
    NSMutableArray *copiedGraph;   //复制一份输入数据
    NSMutableArray *Vreserved = [NSMutableArray array];
    NSMutableArray *Vdeleted = [NSMutableArray array];
    
    copiedGraph = [NSMutableArray arrayWithArray:graphic];
    for (NSUInteger i = 1; i <= graphic.count; i ++) {
        [Vreserved addObject:@(i)];
    }
    
    while (copiedGraph.count > 2) {
        NSUInteger deletedV = contraction(copiedGraph);
        //操作两个顶点数组中的值，从第一个移到第二个
        [Vreserved removeObject:@(deletedV)];
        [Vdeleted addObject:@(deletedV)];
    }
    
    NSLog(@"reserved V: %@",Vreserved);
    NSArray *lastV = [copiedGraph lastObject];
    return lastV.count - 1;
}

int main(int argc, const char * argv[])
{
    @autoreleasepool
    {
        //读取输入数据
        NSMutableArray *graph = getGraphList();
        NSUInteger cross = getMinCut(graph);
        NSLog(@"Result is: %lu",(unsigned long)cross);
    }
    
    return 0;
}
