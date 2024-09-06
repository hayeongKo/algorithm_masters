package BJ17413;

// 17413
// 단어 뒤집기 2

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split("");

        List<String> tag = new ArrayList<>();
        Deque<String> temp = new ArrayDeque<>();
        boolean flag = false;

        for (String spell : input) {
            if (spell.equals("<")) { //태그 시작
                // 태그 시작 전 쌓여있던 스택 비우기
                while (!temp.isEmpty()) {
                    System.out.print(temp.pollLast());
                }
                tag.add(spell);
                // 괄호 flag on
                flag = true;
            } else if (spell.equals(">")) { // 태그 종료
                tag.add(spell);
                System.out.print(String.join("", tag)); // ''.join(list) 랑 똑같은거
                tag.clear();
                // 괄호 flag off
                flag = false;
            } else if (flag) { // 태그 사이에 있을시
                tag.add(spell);
            } else if (spell.equals(" ")) { // 띄어쓰기 기준 스택 비워야하니깐
                while (!temp.isEmpty()) {
                    System.out.print(temp.pollLast());
                }
                System.out.print(" ");
            } else {
                // 그 외에는 그냥 스택에 넣기
                temp.add(spell);
            }
        }

        while (!temp.isEmpty()) {
            System.out.print(temp.pollLast());
        }

    }
}
