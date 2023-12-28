# https://school.programmers.co.kr/learn/courses/30/lessons/60059
def solution(s):
    min_len = len(s)
    for i in range(len(s)-1) :
        unit_str = s[:(i+1)]
        cnt = 1 
        tmp_result = "" 
        # print("\n---- init tmp_result ----")
        for j in range((i+1), len(s), (i+1)) : 
            # print("\nunit_str : ", unit_str, end=" ")
            # print(", s[j:(j+(i+1))] : ", s[j:(j+(i+1))])
            if unit_str == s[j:(j+(i+1))] :
                cnt += 1
                # print("cnt : ", cnt)
            else :
                cnt_str = str(cnt)
                if cnt == 1:
                    cnt_str = ""
                tmp_result += cnt_str + unit_str #+ s[j:]
                # print("tmp_result :", tmp_result)
                unit_str = s[j:(j+(i+1))]
                # print("next str : ", unit_str)
                cnt = 1
                
            # print("unit_str 길이 : ", len(unit_str))
            # print("남은 문자열 길이: ", len(s) -1 - j)
            if len(unit_str) > len(s) -1 -j  :
                cnt_str = str(cnt)
                if cnt == 1:
                    cnt_str = ""
                tmp_result += cnt_str + unit_str
                # print("tmp_result :", tmp_result)
                break
        
        if len(tmp_result) < min_len :
            min_len = len(tmp_result)
            # print("cur min_len : ", min_len)
            
    # print("result : ", min_len)
    return min_len