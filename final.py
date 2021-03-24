def count_sales(masks, gloves):
    gloves = gloves
    mask = masks

    unique_gloves = list(dict.fromkeys(gloves))
    unique_masks = list(dict.fromkeys(mask))
    #print(unique_gloves)
    #print(unique_masks)
    count_list = []
    for i in  unique_gloves:
        counts = gloves.count(i)
        count_list.append(counts)
    pair = []
    for i in count_list:
        if i % 2 != 0:
            i = i-1
            pair.append(i)
        else:
            pair.append(i)
    answer_list = []
    sell = list(set(unique_masks) & set(pair))
    for i in pair:
        answer_list.append(i/2)
    #print(sum(answer_list))

    #mask
    mask_list = []
    for m in unique_masks:
        counts = mask.count(m)
        mask_list.append(counts)
    unique_gloves.sort()
    unique_masks.sort()

    #print(answer_list)
    #print(mask_list)
    l = len(answer_list)
    sell_list = []
    for i in range(0,l):
        final_sell = min(answer_list[i],mask_list[i])
        sell_list.append(final_sell)
    #print(sell_list)
    print(sum(sell_list))
    f.close()


import json
# f = open('jsonData.json',) 
f = open('jsonData3.json',)
data = json.load(f) 

count_sales(data['masks'], data['gloves'])
  
f.close() 
