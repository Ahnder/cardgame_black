import random

# CardDeck
class CardDeck():
    ''' 52종의 카드를 보유하는 덱  클래스
    초기에 52종의 카드를 셔플해서 랜덤한 순서로 보관한다
    카드 분배 요청이 들어 올 시 1장씩 배분해준다
    배분해준 카드는 덱에 더이상 존재하지 않는다
    '''
    # init
    def __init__(self):
        # 카드덱 초기화 총 52종의 카드를 생성한다
        # suit: 카드의 무늬, deno: 카드의 끗수
        self.card_deck = [
            suit + '_' + deno
            for suit in ['spade', 'heart', 'diamond', 'clover']
            for deno in 'A23456789TJQK'
        ]        
        # 카드덱이 생성되면 카드순서를 무작위로 섞는다
        random.shuffle(self.card_deck)

    
    # 카드를 한장씩 분배하는 메서드
    def draw_card(self):
        return self.card_deck.pop()    


# Gamer
class Gamer():
    ''' 딜러와 플레이어의 부모 클래스
    카드분배를 요청한다
    카드를 받아와서 총 2장씩 보관한다
    2장 초과시엔 먼저 받은 카드부터 버린다
    '''
    # init
    def __init__(self) -> None:
        # 카드를 받아서 손패에 저장 할 빈리스트를 생성
        self.card_in_hand = list()


    # 덱에서 분배해준 카드를 받아서 손패에 저장
    # 손패에 카드가 2장이면 제일 먼저 받은 카드를 버리고 새로운 카드를 추가
    def receive_card(self, card):
        if len(self.card_in_hand) >= 2:
            self.card_in_hand.pop(0)
        self.card_in_hand.append(card)    


# GameRule
class GameRule():
    ''' 점수계산 요청이 들어오면 점수계산을 해서 리턴해준다
    게임이 종료되면 각 점수를 비교해서 승패를 판단해준다
    '''
    pass



# main
if __name__ == '__main__':

# 메인함수 진행 순서
#
# 1) 각 클래스로 객체를 생성한다
# 1-1) 카드덱은 순서가 랜덤한 52종의 카드가 담긴 리스트를 생성한다 (__init__)
# 1-2) 게이머객체는 딜러와 플레이어 두 객체를 따로 생성한다(본인들의 손패를 빈리스트로 생성) (__init__)
#
# 2) 카드덱에서 플레이어와 딜러에게 번갈아가며 카드 한장씩 총 두장을 각각 배분한다 
#   (카드덱에서 한장씩 분배하는 메서드, 게이머가 카드를 받아 자신의 손패에 저장하는 메서드 작성)
#
# 3) 플레이어는 현재 손패의 카드를 확인하고 카드를 더 추가할지 결정한다 (while)
#   (카드를 추가하면 반복문 진행, 추가하지 않으면 반복문 탈출)
# 3-1) 플레이어가 카드를 추가하면 
#      딜러는 본인 손패 카드의 점수계산을 요청한다(게임룰에서 점수계산 메서드로 구현)
# 3-2) 딜러는 본인의 점수기준에 따라서 카드 추가 여부를 결정한다(딜러클래스에 따로 메서드 구현)
#
# 4) 플레이어와 딜러의 현재 손패카드의 점수를 비교하여 승패를 판단한다
#   (게임룰에서 메서드로 구현)
#
# 5) 승패여부 터미널화면에 출력

    deck = CardDeck()
    dealer = Gamer()
    player1 = Gamer()
    print('카드덱:\n', deck.card_deck)
    
    # 카드를 한장씩 두번 배분한다
    # 현재는 range 안에 2라는 숫자가 하드코딩 되어 있는데 차후 변수로 바꿀예정
    for i in range(2):
        player1.receive_card(deck.draw_card())
        dealer.receive_card(deck.draw_card())

    print(player1.card_in_hand)
    print(dealer.card_in_hand)
