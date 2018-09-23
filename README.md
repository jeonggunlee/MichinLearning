## MichinLearning 스터디 동아리입니다: Machine Learning을 함께 공부합니다!

```미친 러닝``` 스터디 그룹입니다. 한림대학교 소프트웨어융합대학 학부생 5명과 대학원생 1명 박사후 연구원 1명 및 교수 1인으로 구성된 모임입니다.
시대의 큰 흐름 중 하나인 인공지능/기계학습 등에 대해서 함께 공부하고 토의합니다.

*  *  *

1차적으로 모임에서는 김성훈 교수의 모두의 딥러닝을 시청후 모여 다양한 토론을 진행합니다.

   - [모두를 위한 머신러닝/딥러닝 강의](https://hunkim.github.io/ml/)
   - 추가적인 동영상 참고자료 ! [테리의 딥러닝 토크](https://www.youtube.com/watch?v=D4zqigCb8co&list=PL0oFI08O71gKEXITQ7OG2SCCXkrtid7Fq)

   - 임승현 추천 [ML Book](https://github.com/jeonggunlee/MichinLearning/blob/master/Machine-Learning.pdf)
*  *  *
**1차 모임: 9월 6일 목요일**: 함께 동영상 시청 - 이후 모임에서는 시청후 토론 방식으로 진행하는 것으로 정함

*  *  *

9월 10일 - "학과 세미나 참가" : 4차산업혁명과 오픈소스 기반 머신러닝 기술 by 최권택 (강남대학교)

*  *  *

**2차 모임: 9월 13일 목요일**

잘문1) training set, validation set, 그리고 test set의 차이

   - 참조: [#1.1. Training / Test / Validation Set : 오버피팅을 피하는 방법](https://www.youtube.com/watch?v=GtLe9Z2No28&index=7&list=PL0oFI08O71gKEXITQ7OG2SCCXkrtid7Fq)

     - validation test set과의 차이점은 test set은 모델의 '최종 성능' 을 평가하기 위해서 쓰이며, training의 과정에 관여하지 않는 차이가 있습니다. 반면 validation set은 여러 모델 중에서 최종 모델을 선정하기 위한 성능 평가에 관여한다 보시면됩니다. 따라서 validation set은 training과정에 관여하게 됩니다. 즉, validation set은 training 과정에 관여를 하며, training이 된 여러가지 모델 중 가장 좋은 하나의 모델을 고르기 위한 셋입니다. test set은 모든 training 과정이 완료된 후에 최종적으로 모델의 성능을 평가하기 위한 셋입니다. 만약 test set이 모델을 개선하는데 쓰인다면, 그건 test set이 아니라 validation set입니다. 만약 여러 모델을 성능 평가하여 그 중에서 가장 좋은 모델을 선택하고 싶지 않은 경우에는 validation set을 만들지 않아도 됩니다. 하지만 이 경우에는문제가 생길 것입니다. (test accuracy를 예측할 수도 없고, 모델 튜닝을 통해 overfitting을 방지할 수도 없습니다.) [출처](http://3months.tistory.com/118 [Deep Play])
     
     - training 과정에 관여한다는 것이 성능을 평가한다는 것이지, 모델의 수정하는데 사용한다는 말은 아닌것 같네요!
    
   - [참조](https://stats.stackexchange.com/questions/19048/what-is-the-difference-between-test-set-and-validation-set):
    
     - The training set is used to fit the models; the validation set is used to estimate prediction error for model selection; the test set is used for assessment of the generalization error of the final chosen model. Ideally, the test set should be kept in a “vault,” and be brought out only at the end of the data analysis.

*  *  *
**3차 모임: 9월 17일 월요일**

잘문1) cross-entropy를 cost 함수로 활용하는 이유 ? 그리고 cross-entropy와 Mean squre error가 같다고(?)하던데 어떻게 같은건가라는 질문에 답을 해줄수 있는 글인것 같네요. 한번 읽어 보면 좋을 것 같네요.
   - [Neural Networks의 학습속도 저하(Slowdown)를 막는 Cross-Entropy Cost Function](http://solarisailab.com/archives/2237)
   - [Cross Entropy의 정확한 확률적 의미](https://taeoh-kim.github.io/blog/cross-entropy%EC%9D%98-%EC%A0%95%ED%99%95%ED%95%9C-%ED%99%95%EB%A5%A0%EC%A0%81-%EC%9D%98%EB%AF%B8/)
   - [A Short Introduction to Entropy, Cross-Entropy and KL-Divergence](https://www.youtube.com/watch?v=ErfnhcEV1O8)

>[재밌는 아이디어] 사실 어디 회사분이 아이들이 아빠 엄마를 인식하는 것과 유사하게 아빠 사진 엄마 사진 등이 캡쳐될때마다 (아빠라는 소리가 들릴때 카메라를 찍어서 찍힌 사진에서 얼굴을 검출하고, 아빠라고 labelling 함) online learning을 해서 사람들을 인식해가는 걸 만들어보고 싶다고 했는데...9장이 이런 부분에 사용될 수 있을 것 같네요. 클라우드도 사용하구~ ㅋㅋ


*  *  *
**2018년 9월 20일**

질문1) 딥모델을 구성할때, layer를 증가시키는 거와 layer에서 node / weight를 증가시키는 것에 대한 효과 ?
어떤 것이 더 효과적일까 ?
   - 이미지의 경우 layer의 노드수가 중요하지 않을까?
   - 근데 왜 최근 모델은 layer에 집중할까?
   - http://playground.tensorflow.org 시뮬레이션 해보면 어떨까?
   - [Stackoverflow](https://stackoverflow.com/questions/35520587/how-to-determine-the-number-of-layers-and-nodes-of-a-neural-network)
      > As Yoshua Bengio, Head of Montreal Institute for Learning Algorithms remarks:
      > "Very simple. Just keep adding layers until the test error does not improve anymore."
      >
      >
      > A method recommended by Geoff Hinton is to add layers until you start to overfit your training set. Then you add dropout or another regularization method.

질문2) Back-Propagation할때 0이 나오면 어떻게 처리하는가?
       if( error == 0 ) error = MIN;

*  *  *
**2018년 9월 27일** : **Convolutional Neural Networks**

질문1) ?


*  *  *
### 참여자 리스트입니다.
- 소프트웨어 융합 대학 교수 이정근 [http://www.onchip.net](http://www.onchip.net)
- 컴퓨터공학과 대학원 Nguyen Van Toan 박사
- 컴퓨터공학과 대학원 김용휘 (석사과정)
- 소프트웨어 융합 대학 학부생: 임병준, 임승현, 이종학, 정재민, 김민정


