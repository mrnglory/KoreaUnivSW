# 어느 하나라도 접두어가 되는 쌍이 존재하는 전화번호
# 문제에 주어지는 데이터의 크기로 성능 힌트를 얻는다
# 전화번호의 갯수가 1,000,000개 이하 -> O(n*log(n)) or O(n)이어야 함
# O(n*log(n)): binary search, quick sort, heap queue
# 정렬되지 않은 입력값이므로 binary search 제외
# 이 문제는 최대 최소 값을 묻지 않으므로 heap queue 제외
# 스트링 정렬 시 맨 앞의 아스키코드 값 기준임
# 접두어 관계의 쌍은 정렬 시 서로 붙어있거나 인접해있음
# 이 문제는 모든 접두어 쌍을 찾으라는 것이 아니기 때문에 단 하나라도 존재하는지의 여부만 조사하면 됨
def solution(phoneBook):
    phoneBook.sort()
    for i in range(len(phoneBook) - 1):
        if phoneBook[i + 1].startswith(phoneBook[i]):
            return False
    return True