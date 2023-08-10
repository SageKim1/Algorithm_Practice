class Solution:
    # Approach 2: Sliding Window
    # time complexity: O(n)
    # space complexity: O(min(m, n))
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Counter 객체 초기화
        chars = Counter()

        # 가장 긴 substring의 좌, 우측 index
        left = right = 0

        res = 0 # 가장 긴 substring의 길이
        while right < len(s): # 우측 index가 string을 넘어가지 않음
            r = s[right] # right index의 글자
            chars[r] += 1 # 해당 글자의 cnt 증가

            while chars[r] > 1: # 해당 글자의 cnt가 2 이상
                l = s[left] # 좌측 index의 글자
                chars[l] -= 1 # 해당 글자의 cnt 감소
                left += 1 # 좌측 index를 한칸 우측으로 이동

            res = max(res, right - left + 1) # max 길이 다시 계산

            right += 1 # 우측 index를 한칸 우측으로 이동
        return res
