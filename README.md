### 파이썬 클래스를 이용한 블랙잭 게임

- 블랙잭의 규칙을 간소화한 파이썬 프로그램
- 게임은 전부 터미널로 진행한다

<br>


<!-- 목차 생성 -->
### 목차:
1. [게임 규칙](#1-게임-규칙)
2. [객체들의 속성과 역할](#2-객체들의-속성과-역할)
3. [클래스와 게임진행순서 설계](#3-클래스와-게임진행순서-설계)


<br>


### 1. 게임 규칙

- 카드덱은 총 52장의 카드로 구성(무늬와 끗수를 곱한 총 52가지의 카드)
    - suit(무늬): spade, heart, diamond, clover
    - deno(끗수): A, 2~9, T, J, Q, K
    - 점수는 A는 1점, 2-9의 숫자는 값 그대로 점수로 쓰고 나머지 T,J,Q,K는 10점으로 한다
- 게임을 시작하면 딜러와 플레이어는 덱에서 카드를 한장씩 두번 배분받아 총 2장을 소지한다
    - 카드는 딜러와 플레이어 번갈아서 순차적으로 배분받는다
- 게임의 간소화를 위해 딜러와 플레이어 모두 카드를 하나 추가하면 제일 먼저 추가 된 카드를 손패에서 버린다
    - 예를들어 1번카드와 2번카드 두장을 가지고 있고 3번카드 한장을 추가하면 1번카드를 버리고 손패에 2번카드와 3번카드가 남는다
- 플레이어는 본인의 희망여부에 따라 카드를 더 뽑을지 그만둘지 결정할 수 있다
- 딜러는 본인 카드 두개의 점수가 16점 이하면 카드 하나를 추가하고, 17점 이상이면 추가하지 않는다
- 플레이어가 더 이상 카드를 추가하지 않기로 결정하면 딜러와 플레이어 카드 두장의 점수를 계산하여 21에 근사한 사람이 승리한다

<br>


<br>

### 2. 객체들의 속성과 역할

- CardDeck
    - 총 52장의 카드로 구성 된 리스트를 가지고 있다
    - 52장의 카드는 객체가 만들어지는 순간 무작위로 재배치된다
    - 요청이 올 시 카드를 한장씩 배분한다(배분 된 카드는 덱에서 없어진다)
- Gamer
    - 딜러와 플레이어의 부모 클래스
    - 카드를 배분 받아서 본인 손패에 저장한다(리스트)
    - 딜러는 현재 카드 두장의 점수에 따라 카드추가가 결정된다
    - 플레이어는 본인의사에 따라 카드추가를 요청 할 수 있다
- GameRule
    - 게임 참가자의 현재 점수를 계산해서 반환해준다
    - 게임이 종료되면 게임 참가자의 점수를 비교해서 승패판단을 한다

<br>

### 3. 클래스와 메인함수 순서 설계
- 설계한 메인함수 순서에 맞춰 클래스와 메서드를 작성한다


<br>


<img width="630" alt="design_class_and_sequence" src="https://github.com/Ahnder/cardgame_black/assets/39118212/e888fa10-c5e8-46e9-8a78-670ce475adea">


<br>


### 4. 코드 구현 과정

[<img width="496" alt="스크린샷 2023-10-07 오후 6 32 39" src="https://github.com/Ahnder/cardgame_black/assets/39118212/fd4dc6f5-266f-4e2b-bdbc-2840f2ac2f1d">](https://www.notion.so/03fdfdd8740f489188e9c7a44c11a4d0?pvs=4)


<br>


[코드구현과정 노션페이지](https://www.notion.so/03fdfdd8740f489188e9c7a44c11a4d0?pvs=4)

과정이 길어져서 노션페이지에 작성하였습니다. 이미지 또는 위의 노션페이지 링크를 클릭해주세요! 


<br>

