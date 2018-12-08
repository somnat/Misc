 def charSpaceRemove(string):
         st = string.split()
         one_len = []
         mid_list = []
         for i, word in enumerate(st):
             if len(word) == 1:
                 one_len.append(i)
         mid_list.append("".join(st[one_len[0]:one_len[-1]+1]))
         stri = st[:one_len[0]] + mid_list + st[one_len[-1]+1:]
         return "".join(stri)
