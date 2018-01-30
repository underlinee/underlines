import os
from unittest import TestCase

from underlines import rodriguez
from underlines.common import config
from underlines.domain import book
sentences = ["""인간의 왕조가 흥망성쇠를 거듭하는 동안 이 작은 씨앗은 미래에 대한 희망을 버리지 않고 고집스럽게 버틴 것이다.    
                    그러다가 어느 날 그 작은 식물의 열망이 어느 실험실 안에서 활짝 피었다. 그 연꽃은 지금 어디 있을까. 모든 시작은 기다림의 끝이다.
                    우리는 모두 단 한 번의 기회를 만난다. 우리는 모두 한 사람 한 사람 불가능하면서도 필연적인 존재들이다. 
                    모든 우거진 나무의 시작은 기다림을 포기하지 않은 씨앗이었다.""",
        """위쪽에서는 개울도 숨을 죽이고 있었다. 바위 사이로 사라져 지하로 흘러가는 지점이었다. 
        훨씬 낮은 음으로 분지에 불어오는 바람 소리가 들리기 시작했다. 호수는 움직이는 밤하늘이었다. 바람은 잔물결을 이쪽에서 저쪽 해안으로 밀어냈고, 
        까만 물 위의 물결을 따라 펼쳐진 별빛은 사라지고 나타나기를 반복하다가 갑작스레 방향을 바꾸곤 했다.나는 그대로 멈춰서 그 그림같은 광경을 바라보았다. 
        인간이 없을 때의 산의 삶을 체험한 것 같았다. 나는 방해가 되지 않게 있었고 거기서 제법 환영받는 손님이었다. 이런 산이 나와 함께 있어준다면 외롭지 않을 거라고 다시금 깨닫게 되었다."""]

MODEL_PATH = config.get("MODEL_PATH")

class TestTrain(TestCase):
    def test_train(self):
        rodri = rodriguez.Rodriguez()
        if not os.path.exists(MODEL_PATH):
            rodri.build(sentences)
        rodri.train(sentences)

    def test_build(self):
        rodri = rodriguez.Rodriguez()
        if os.path.exists(MODEL_PATH):
            os.remove(MODEL_PATH)
        rodri.build(sentences)

    def test_is_valid_token_invalid(self):
        assert rodriguez._is_valid_token(("TEST", "INVALID")) == False

    def test_is_valid_token(self):
        assert rodriguez._is_valid_token(("여사", "Noun")) == True

    def test_get_underlines_all(self):
        descriptions = book.get_descriptions()

        rodri = rodriguez.Rodriguez()
        rodri.build(descriptions)

        rodri.show_me_your_brain()
        print(rodri.ask("맛"))