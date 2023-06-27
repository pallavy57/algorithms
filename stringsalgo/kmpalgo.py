# if we know the i is the iteration number, len = lps[i-1] and str[len] == str[i] then lps[i] = len + 1

# when i = 0 len = 0, compare str[len], str[i] if equal then lps[i] = len + 1
# when i = 1 len = 0 compare
# when i = 2 len = 1 compare str[len] and str[i], equal lps[i] = len + 1
# when i = 3 len = 1 compare str[len] and str [i] if not equal then
# when len = 0 (lps[i-1]) means  lps[i] = 0
# when len > 0 then len = lps[len -1 ] where len is lps value of i -1 len = lps[i-1]
#https://medium.com/@aakashjsr/preprocessing-algorithm-for-kmp-search-lps-array-algorithm-50e35b5bb3cb
def fillLPS(str,n):  
    lps = [0 ]* n #LPS[0] of any pattern is always 0 as a string of length 1 would just have “” and a proper prefix and suffix.
    i = 1
    lens = 0 # maintains the length of the longest prefix found so far 
    while (i < len(str)):
        if (str[lens] == str[i]): #we found a new and longer prefix that matches the suffix
            lens = lens + 1 
            lps[i] = lens # move the length to prev to next index
            i += 1 #after we found the match we are moving ahead
        else:
            if lens == 0:
                lps[i] = 0
                i = i + 1
            else:
                #since not matching the length of the longest prefix cant move forward 
                # so we start look one step back in the string longest prefix and index increment is stopped to move further as well
                lens = lps[lens - 1] 


str = "AAABAAAAC" 
n = len(str)   
fillLPS(str,n)                
