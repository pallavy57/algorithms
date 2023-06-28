# if we know the i is the iteration number, len = lps[i-1] and str[len] == str[i] then lps[i] = len + 1

# when i = 0 len = 0, compare str[len], str[i] if equal then lps[i] = len + 1
# when i = 1 len = 0 compare
# when i = 2 len = 1 compare str[len] and str[i], equal lps[i] = len + 1
# when i = 3 len = 1 compare str[len] and str [i] if not equal then
# when len = 0 (lps[i-1]) means  lps[i] = 0
# when len > 0 then len = lps[len -1 ] where len is lps value of i -1 len = lps[i-1]
#https://medium.com/@aakashjsr/preprocessing-algorithm-for-kmp-search-lps-array-algorithm-50e35b5bb3cb
def fillLPS(pat):  
    lps = [0 ]* len(pat) #LPS[0] of any pattern is always 0 as a string of length 1 would just have “” and a proper prefix and suffix.
    i = 1
    lens = 0 # maintains the length of the longest prefix found so far 
    while (i < len(pat)):
        if (pat[lens] == pat[i]): #we found a new and longer prefix that matches the suffix
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
    return lps            

txt="ababcababaad"
pat = "ababa" 
n = len(txt)   
print(fillLPS(pat)) 

def pattern_matching(pat, txt):
    match_indices = []
    n = len(txt)
    m = len(pat)
    lps = fillLPS(pat)
    i = j = 0
    while(i<n): # the longest array
        #keep the i to j
        #1check if characters are matching from start of the pattern to last and check if pattern[j] == txt [i]
        if(pat[j] == txt[i]): #match found then increment cursors in both the arrays
            i +=1
            j +=1
        if(j==m): #cursor has travelled the entire pattern return the matching index
            match_indices.append(i-j)
            j = lps[j-1]   # we have to move ahead to look for other  
        #2once mismatching is found within the pattern then execute this
        # move the j by consulting lps array
        # go to the index of last matched character that is j-1 then where is j-1 in lps array so j = lps[j-1]
        # dont change i compare j = lps[j-1] and i by keeping index of j-1 of pattern array under i of text array and match both    
        if(i<n and pat[j] != txt[i]):
            #if j = o then meaning we are staring from pattern 0 and if dont match then increment i
            #if match then increment both
            if(j==0):
                i = i+1
            else:
                j = lps[j-1]  

    return match_indices                 

print(pattern_matching(pat, txt))

