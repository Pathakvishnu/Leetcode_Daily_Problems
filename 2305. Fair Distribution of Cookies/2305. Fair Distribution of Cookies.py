
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        current_dist = [0]*k # distribution w.r.t to current state
        num_cookies_bag = len(cookies) # number of cookies bag

        def explore_all_option(bag_idx:int,num_child_with_no_cookie:int):
            if num_cookies_bag - bag_idx < num_child_with_no_cookie:
                return float('inf')

            if num_cookies_bag==bag_idx:
                return max(current_dist)

            ans = float('inf')
            for j in range(k):

                num_child_with_no_cookie-=int(current_dist[j]==0)

                current_dist[j]+=cookies[bag_idx]

                ans = min(ans,explore_all_option(bag_idx+1, num_child_with_no_cookie))

                current_dist[j]-=cookies[bag_idx]

                num_child_with_no_cookie+=int(current_dist[j]==0)

            return ans

        return explore_all_option(0,k)
