//
//  main.m
//  AlgorithmsWeek4
//
//  Created by Hanying Zhang on 15/11/13.
//  Copyright © 2015年 myself. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{
    @autoreleasepool
    {
        //1.读取文件内容，建立图的表示
        char fileName[] = "/Users/hanying/Desktop/SCC.txt";
        
        FILE *fp;
        if ((fp = fopen(fileName, "r")) == NULL) {
            NSLog(@"Can not open file!");
            return -1;
        }
        char graph[1000000][5];
        for (int i = 0; i < 1000000; i ++) {
            for (int j = 0; j < 1000000; j ++) {
                graph[i][j] = '0';
            }
        }
        while (!feof(fp)) {
            char line[50];
            fgets(line, 50, fp);
            NSString *oneLine = [NSString stringWithCString:line encoding:NSUTF8StringEncoding];
            oneLine = [oneLine substringToIndex:oneLine.length - 2];
            NSArray *LineNumbers = [oneLine componentsSeparatedByString:@" "];
            int index = [[LineNumbers firstObject] intValue] - 1;
            int vetex = [[LineNumbers lastObject] intValue] - 1;
            
            graph[index][vetex] = '1';
        }
        
        fclose(fp);
        
        //2.进行第一遍Topological Sorting
        
        //3.逆向图
        
        //4.根据第一遍topological sorting的结果进行第二遍DFS
        
        //5.输出前五个最大的SCC的size
    }
    return 0;
}
