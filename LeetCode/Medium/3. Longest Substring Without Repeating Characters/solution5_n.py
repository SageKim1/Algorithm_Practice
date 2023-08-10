class Solution:
    # ASCII
    # time: O(n)
    # space: O(m) | 문자열 내에 사용된 문자의 종류 수
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128 # 128개의 ASCII 문자에 대한 인덱스
        left = right = 0 # 슬라이딩 윈도우의 왼쪽과 오른쪽 인덱스
        res = 0 # 가장 긴 중복 없는 부분 문자열의 길이

        while right < len(s): # 문자열의 끝에 도달할 때까지
            r = s[right] # 현재 위치의 문자
            index = chars[ord(r)] # r의 ASCII 코드에 해당하는 값의 인덱스
            # 중복 발생 <= 현재 문자가 이전에 등장 & 현재 슬라이딩 윈도우 내의 위치
            if index is not None and left <= index < right:
                # 중복된 문자 이전의 위치 다음 인덱스부터 다시 부분 문자열을 찾기
                left = index + 1
            
            res = max(res, right - left + 1) # 부분문자열 길이 계산

            chars[ord(r)] = right # 현재 문자의 인덱스 저장
            right += 1
        return res
