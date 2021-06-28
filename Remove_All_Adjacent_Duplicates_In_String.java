// 20210628
// LeetCode

/* FIRST APPROACH - user-defined stack
 * Runtime: 4ms
 * Memory Usage: 39.6 MB */
class Solution {
    public String removeDuplicates(String s) {
        char[] stack = new char[s.length()];
        stack[0] = s.charAt(0);
        int top = 0;
        for(int i = 1; i < s.length(); ++i){
            char c = s.charAt(i);
            if((top >= 0)&&(stack[top] == c)) --top;
            else stack[++top] = c;
        }
        return new String(stack, 0, top + 1);
    }
}

/* SECOND APPROACH - import stack
 * Runtime: 131ms
 * Memory Usage: 41.3 MB */
/*
import java.util.Stack;
class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        stack.push(s.charAt(0));
        for(int i = 1; i < s.length(); ++i){
            char c = s.charAt(i);
            if(!stack.empty()&&(stack.peek() == c)) stack.pop();
            else stack.push(c);
        }
        String ret = "";
        while(!stack.empty()) ret = stack.pop() + ret;
        return ret;
    }
}
*/
