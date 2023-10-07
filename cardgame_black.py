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
    def __init__(self):
        # 카드를 받아서 손패에 저장 할 빈리스트를 생성
        self.card_in_hand = list()
        # 현재 규칙 사항인 손패의 총 카드수를 변수로 생성
        self.limit_card_amount = 2
        # 손패가 2장일 시 버릴 제일 먼저 받은 카드의 인덱스를 변수로 생성
        self.out_hand_index = 0


    # 덱에서 분배해준 카드를 받아서 손패에 저장
    # 손패에 카드가 2장이면 제일 먼저 받은 카드를 버리고 새로운 카드를 추가
    def receive_card(self, card):
        if len(self.card_in_hand) >= self.limit_card_amount:
            self.card_in_hand.pop(self.out_hand_index)
        self.card_in_hand.append(card)    


# Dealer
class Dealer(Gamer):
    ''' Gamer 클래스를 상속받은 클래스
    딜러만의 규칙: 총 카드 점수가 16이하면 카드를 한장 더 추가하고
               17이상이면 카드를 더 이상 추가하지 않는다           
    '''
    # 카드를 추가할지 결정하는 메서드
    # GameRule 클래스의 점수계산 메소드에 계산을 요청하여 받은 점수를 가지고 결정한다
    def decide_to_receive_card(self, score):
        # 현재 규칙하의 점수 기준 변수
        add_to_card_score = 16 
        # 점수가 기준을 초과하면 False, 16이하면 True를 리턴
        if score > add_to_card_score:
            return False
        else:
            return True


# GameRule
class GameRule():
    ''' 점수계산 요청이 들어오면 점수계산을 해서 리턴해준다
    게임이 종료되면 각 점수를 비교해서 승패를 판단해준다
    '''
    # 점수 규칙을 초기화 메서드에 작성해서 관리
    def __init__(self):
        # 점수 기준 딕셔너리
        # 문자열의 숫자는 그 숫자에 맞는 정수형 값 
        # A는 1점, JKQ는 10점
        self.score_rule_dict = {
            'A': 1, 'T': 10, 'J': 10, 'Q': 10, 'K': 10,
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }
        # 현재 카드의 형태는 spade_9 같은 문자열이므로 
        # 문자열의 가장 마지막 문자를 값으로 가져오기 위한 변수
        self.deno_value = -1
    
    
    # 요청이 들어온 카드리스트 점수계산을 한다.
    def cal_score(self, cardlist):
        # sum을 이용하여 카드의 점수를 계산한다
        score = sum(
            self.score_rule_dict[card[self.deno_value]]
            for card in cardlist
        )
        return score
    

    # 두개의 카드리스트를 받아서 점수를 비교, 승리한 쪽의 카드리스트를 반환한다
    def compare_score(self, cardlist1, cardlist2):
        # 카드리스트를 내부함수인 cal_score를 사용해서 점수를 계산한다
        deck1_score = self.cal_score(cardlist1)
        deck2_score = self.cal_score(cardlist2)
        # if문으로 점수를 비교해서 승리한 쪽의 카드리스트를 반환
        if deck1_score > deck2_score:
            return cardlist1
        elif deck1_score < deck2_score:
            return cardlist2
        else:
            return


# main
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
if __name__ == '__main__':
    deck = CardDeck()
    dealer = Dealer()
    player1 = Gamer()
    rule = GameRule()
    #print('카드덱:\n', deck.card_deck)
    
    # 카드를 한장씩 두번 배분한다
    # 현재는 range 안에 2라는 숫자가 하드코딩 되어 있는데 차후 변수로 바꿀예정
    for i in range(2):
        player1.receive_card(deck.draw_card())
        dealer.receive_card(deck.draw_card())


    # 플레이어에게 카드 추가 여부를 물어보고 딜러 또한 카드 추가를 결정한다
    while True:
        # 플레이어에게 현재 보유 카드를 출력해준다
        print('플레이어 현재 보유 카드: ', player1.card_in_hand) 

        add_card_answer = input('카드를 추가하시겠습니까? (y/n): ')
        # 플레이어가 카드를 추가하지 않을 경우 반복문을 탈출해서 승패판단읋 진행한다
        if add_card_answer == 'n':
            break
        # 플레이어가 카드를 추가하는 경우, 이 단계에서 딜러도 카드 추가여부를 결정한다
        elif add_card_answer == 'y':
            player1.receive_card(deck.draw_card())
            
            # 현재 딜러의 점수를 계산하고
            # 그 점수를 추가여부판단 메서드에 변수로 넣어
            # 반환되는 값이 True면 카드를 추가하고 False면 추가하지 않는다
            dealer_score = rule.cal_score(dealer.card_in_hand)
            if dealer.decide_to_receive_card(dealer_score):
                dealer.receive_card(deck.draw_card())
        # 입력 값이 y 또는 n 이 아닐 경우 안내문 출력 후 반복문의 처음으로 돌아간다
        else:
            print('잘못 된 입력입니다')
            continue



    # 승패를 판단해서 출력해준다
    win_deck = rule.compare_score(player1.card_in_hand, dealer.card_in_hand)
    if not win_deck:
        print('무승부입니다.')
    elif win_deck is player1.card_in_hand:
        print('플레이어가 승리했습니다')
    elif win_deck is dealer.card_in_hand:
        print('딜러가 승리했습니다')
    else:
        print('승패판단과정에서 에러발생')            

    print('플레이어1 손패: ', player1.card_in_hand, '플레이어1 점수: ', rule.cal_score(player1.card_in_hand))
    print('딜러 손패: ', dealer.card_in_hand, '딜러 점수: ', rule.cal_score(dealer.card_in_hand))
