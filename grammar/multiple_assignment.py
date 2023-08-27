"""
다중 할당을 해야만 하는 경우가 있을 수 있음

ex) rev, rev.next, slow = slow, rev, slow.next 구문을

rev, rev.next = slow, rev
slow = slow.next 로 분리해서 표현할 경우,

rev = slow 구문이 먼저 적용되고
python은 원시 타입 없이 모두가 객체이므로 참조 변수로 할당된다.
-> slow와 rev가 동일 참조

값을 할당하는 것이 아니라, 불변 객체에 대한 참조를 할당
"""
#
# print(id(5))
#
# a = 6
# print(id(a))
#
# b = 6
# print(id(b))

"""
2909963616624
2909963616624
2909963616624

1737519137136
1737519137168
1737519137168
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


rev = 1
# 연결 리스트 생성 : 2 -> 3
node2 = ListNode(2)
node3 = ListNode(3)
node2.next = node3
# print(node2)
"""
다중 할당시 하나의 트랜잭션으로 진행
"""
slow = node2
rev, rev.next, slow = slow, rev, slow.next
# print(rev)
# print(rev.next)
# print(slow)
# print(rev.val)
# print(slow.val)

"""
나눠서 처리하는 경우
rev, rev.next = slow, rev
rev = 2->3, rev.next = 1이므로 rev 가 2->1이 됨

앞에서는 slow = slow.next까지 하나의 트랜잭션에 적용되므로
slow가 3, None 이어야 하는데

여기서 rev = slow로 같은 곳을 바라보니까 2->1이 됨

"""
rev, rev.next = slow, rev
print(rev)
print(slow)
# rev와 slow가 같은 값을 바라봄

slow = slow.next
print(slow.val)
print(slow.next)
