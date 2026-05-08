# -- 3629. Minimum Jumps to Reach End via Prime Teleportation
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

class Solution {
    public int minJumps(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return 0;
        }

        int maxValue = 1;
        for (int num : nums) {
            maxValue = Math.max(maxValue, num);
        }

        int[] spf = buildSmallestPrimeFactor(maxValue);
        Map<Integer, List<Integer>> edges = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int value = nums[i];

            while (value > 1) {
                int prime = spf[value];
                edges.computeIfAbsent(prime, key -> new ArrayList<>()).add(i);

                while (value % prime == 0) {
                    value /= prime;
                }
            }
        }

        boolean[] seen = new boolean[n];
        Queue<Integer> queue = new ArrayDeque<>();
        seen[0] = true;
        queue.offer(0);
        int jumps = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int step = 0; step < size; step++) {
                int index = queue.poll();

                if (index == n - 1) {
                    return jumps;
                }

                if (index > 0 && !seen[index - 1]) {
                    seen[index - 1] = true;
                    queue.offer(index - 1);
                }

                if (index + 1 < n && !seen[index + 1]) {
                    seen[index + 1] = true;
                    queue.offer(index + 1);
                }

                int value = nums[index];
                if (value >= 2 && spf[value] == value) {
                    List<Integer> targets = edges.remove(value);

                    if (targets != null) {
                        for (int next : targets) {
                            if (!seen[next]) {
                                seen[next] = true;
                                queue.offer(next);
                            }
                        }
                    }
                }
            }

            jumps++;
        }

        return -1;
    }

    private int[] buildSmallestPrimeFactor(int maxValue) {
        int[] spf = new int[maxValue + 1];

        for (int i = 2; i <= maxValue; i++) {
            if (spf[i] != 0) {
                continue;
            }

            spf[i] = i;

            if ((long) i * i > maxValue) {
                continue;
            }

            for (long j = (long) i * i; j <= maxValue; j += i) {
                if (spf[(int) j] == 0) {
                    spf[(int) j] = i;
                }
            }
        }

        return spf;
    }
}
