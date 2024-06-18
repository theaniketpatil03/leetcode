'''
Question - 

    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

Example - 
    
    Input: ["flower","flow","flight"]
    Output: "fl"

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
'''

def long_comm_pref(vals):
    # print(vals[1:])
    # for ind_of_first_str in range(len(vals[0])):
    #     for string in vals[1:]:
    #         # print(string)
    #         if len(string) <= ind_of_first_str or string[ind_of_first_str] != vals[0][ind_of_first_str]:
    #             return string[:ind_of_first_str]
    #             # print('out of range')

    for index_first_str in range(len(vals[0])):
        for string in vals[1:]:
            if len(string)<=index_first_str:
                print('its same', index_first_str, len(string))
                
    return vals[0]

print(long_comm_pref(["flower","flow","flight"]))
