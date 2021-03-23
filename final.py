# function for count sales of gloves and masks
def count_sales(gloves, masks):
    gloves = gloves
    mask = masks

    unique_gloves = list(set(gloves))

    # print(type(unique_gloves))
    # print(type(unique_masks))

    # print(unique_gloves)
    # print(unique_masks)
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
    for i in pair:
        answer_list.append(i/2)

    print(sum(answer_list))

# load jason 
import json
f = open('jsonData3.json')
data = json.load(f)

# function call
count_sales(data['gloves'], data['masks'])

f.close()