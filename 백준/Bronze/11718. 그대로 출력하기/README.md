# [Bronze III] 그대로 출력하기 - 11718 

[문제 링크](https://www.acmicpc.net/problem/11718) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

구현, 문자열

### 제출 일자

2025년 5월 26일 20:19:12

### 문제 설명

<p>입력 받은 대로 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.</p>

### 출력 

 <p>입력받은 그대로 출력한다.</p>

###  개념
 <p>이 코드가 있는데 실행이 되는지는 잘 모르겠음
  
    import sys
    s = sys.stdin.readlines()
    for i in s:
        print(i.rstrip())
  
    
 
    sys.stdin.readline()
    문자열 형태로 개행문자(\n)를 포함한 한 줄만 입력된다.
    sys.stdin.readlines()
    파일의 끝까지 한번에 읽어온다. 각 줄이 개행문자(\n)가 포함되어 리스트로 저장된다.
    sys.stdin.read()
    파일의 끝까지 한번에 읽어오고 읽은대로 출력된다.
    sys.stdin.read().splitlines()
    파일의 끝까지 한번에 읽어오고 개행문자를 제외하여 리스트로 읽는다.
    
    
    EOF = End Of File 이라는 의미인데, 말 그대로 입력값이 없어지는 상황을 받아준다.</p>
