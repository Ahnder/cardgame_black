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
        # 카드리스트에서 카드를 가져오고
        # 규칙 딕셔너리의 key, value를 items를 이용해서 가져온다
        # 규칙 딕셔너리의 key와 카드의 끗수가 같은 딕셔너리 값을 가져와 합산한다
        score = sum(
            vaule
            for card in cardlist
            for key, vaule in self.score_rule_dict.items()
            if key is card[self.deno_value]
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



if __name__ == '__main__':
    # 1) 각 클래스의 객체 생성
    deck = CardDeck()   # 카드 덱 생성
    dealer = Dealer()   # 딜러 객체
    player = Gamer()    # 플레이어 객체
    rule = GameRule()   # 룰 객체
    
    print('{:-^45}'.format('Black Jack Game Start'))

    # 2) 카드를 한장씩 두번 배분한다
    for i in range(2):
        dealer.receive_card(deck.draw_card())
        player.receive_card(deck.draw_card())

    # 3) 플레이어에게 카드 추가 여부를 묻는 반복문
    while True:
        # 플레이어에게 현재 보유 카드를 출력해주고 카드를 추가할지 선택하게 한다
        print('\n플레이어 현재 보유 카드: ', ' '.join(player.card_in_hand)) 
        #
        add_card_answer = input('카드를 추가하시겠습니까? (y/n): ')
        # 플레이어가 카드를 추가하지 않을 경우 반복문을 탈출해서 승패판단읋 진행한다
        if add_card_answer == 'n':
            break
        # 3-1) 플레이어가 카드를 추가한다
        elif add_card_answer == 'y':
            player.receive_card(deck.draw_card())
            # 3-2) 현재 딜러의 점수를 계산하고
            # 그 점수를 추가여부판단 메서드에 변수로 넣어
            # 반환되는 값이 True면 카드를 추가하고 False면 추가하지 않는다
            dealer_score = rule.cal_score(dealer.card_in_hand)
            if dealer.decide_to_receive_card(dealer_score):
                dealer.receive_card(deck.draw_card())
        # 입력 값이 y 또는 n 이 아닐 경우 안내문 출력 후 반복문의 처음으로 돌아간다
        else:
            print('잘못 된 입력입니다')


    # 4) 승패를 판단한다
    win_deck = rule.compare_score(player.card_in_hand, dealer.card_in_hand)
    # 5) 승패 여부 출력
    if not win_deck:
        print('\n무승부입니다.')
    elif win_deck is player.card_in_hand:
        print('\n플레이어가 승리했습니다')
    elif win_deck is dealer.card_in_hand:
        print('\n딜러가 승리했습니다')
    else:
        print('승패판단과정에서 에러발생')            

    # 플레이어와 딜러의 최종 손패와 점수를 출력한다
    # print('플레이어 손패: ', ' '.join(player.card_in_hand), '점수: ', rule.cal_score(player.card_in_hand))
    # print('딜러 손패: ', ' '.join(dealer.card_in_hand), '점수: ', rule.cal_score(dealer.card_in_hand))
    print((
        '플레이어 손패: ' + ' '.join(player.card_in_hand) + '\t' + '점수: ' + str(rule.cal_score(player.card_in_hand)) + '\n'
        + '딜러 손패: ' + ' '.join(dealer.card_in_hand) + '\t' + '점수: ' + str(rule.cal_score(dealer.card_in_hand)) + '\n'
    ))
    print('{:-^45}'.format('Black Jack Game End'))
