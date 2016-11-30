//: Playground - noun: a place where people can play

import Cocoa

// Read Datas From File
var fileData = [String]()
let fileManager = NSFileManager()
let fileDir = "/users/workMac/Desktop/knapsack1.txt"
if let data = fileManager.contentsAtPath(fileDir){
    let dataString = String.init(data: data, encoding: NSUTF8StringEncoding)
    fileData = (dataString?.componentsSeparatedByString("\n"))!
}
fileData.popLast()

var vwDatas = [[Int]]()
for st in fileData {
    let vw = st.componentsSeparatedByString(" ")
    var vwData = [Int]()
    vwData.append(Int(vw[0])!)
    vwData.append(Int(vw[1])!)
    vwDatas.append(vwData)
}

let W = vwDatas[0][0]
let itemCounts = vwDatas[0][1]
vwDatas.removeAtIndex(0)

// Calculating
var results = [[Int]].init(count: itemCounts, repeatedValue: [Int].init(count: W, repeatedValue: 0))
for i in 1..<itemCounts {
    for x in 0..<W {
        let w = vwDatas[i][1]
        let v = vwDatas[i][0]
        if x < w {
            results[i][x] = results[i-1][x]
        }else{
            results[i][x] = max(results[i-1][x], results[i-1][x-w] + v)
        }
    }
}

// Results
results[itemCounts - 1][W - 1]