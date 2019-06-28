def merge(lists):
    import heapq
    mergeList = []
    heap = [(list[0], i, 0) for i, list in enumerate(lists)]
    heapq.heapify(heap) 

    while heap:
        val, listIndex, elementIndex = heapq.heappop(heap)
        
        mergeList.append(val)
        if elementIndex + 1 < len(lists[listIndex]):
            nextElement = lists[listIndex][elementIndex + 1]
            heapq.heappush(heap, (nextElement, listIndex, elementIndex + 1))
    
    return mergeList

print(merge([[7,8,9,10,300], [1,2,3], [4,5,30,100]]))
