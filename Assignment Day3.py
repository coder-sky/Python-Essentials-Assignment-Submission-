#Consider a person is represented by Pi, where i is the index of the following list.
li = [2, 1, 5, 3, 4]
print("gift_presented_to = ",li)

'''
{Senario}

Person P1 has given gift to person P2
Person P2 has given gift to person P1
Person P3 has given gift to person P5
Person P4 has given gift to person P3
Person P5 has given gift to person P4
'''

li[0],li[1],li[2],li[3],li[4] = li[0],li[1],li[4],li[2],li[3]



print("gift_received_from = ",li)
