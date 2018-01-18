from unittest import TestCase

from underlines import keyword_finder

underline = """인간의 왕조가 흥망성쇠를 거듭하는 동안 이 작은 씨앗은 미래에 대한 희망을 버리지 않고 고집스럽게 버틴 것이다.    
                    그러다가 어느 날 그 작은 식물의 열망이 어느 실험실 안에서 활짝 피었다. 그 연꽃은 지금 어디 있을까. 모든 시작은 기다림의 끝이다.
                    우리는 모두 단 한 번의 기회를 만난다. 우리는 모두 한 사람 한 사람 불가능하면서도 필연적인 존재들이다. 
                    모든 우거진 나무의 시작은 기다림을 포기하지 않은 씨앗이었다."""

class TestKeywordFinder(TestCase):

    def test_analize_entities(self):
        keywords = keyword_finder.find_keyword(underline, 2)
        assert len(keywords) == 2
        assert type(keywords[0]) is str


