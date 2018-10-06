## MichinLearning 스터디 동아리입니다: Machine Learning을 함께 공부합니다!

```미친 러닝``` 스터디 그룹입니다. 한림대학교 소프트웨어융합대학 학부생 5명과 대학원생 1명 박사후 연구원 1명 및 교수 1인으로 구성된 모임입니다.
시대의 큰 흐름 중 하나인 인공지능/기계학습 등에 대해서 함께 공부하고 토의합니다.

*  *  *

1차적으로 모임에서는 김성훈 교수의 모두의 딥러닝을 시청후 모여 다양한 토론을 진행합니다.

   - [모두를 위한 머신러닝/딥러닝 강의](https://hunkim.github.io/ml/)
   - 추가적인 동영상 참고자료 ! [테리의 딥러닝 토크](https://www.youtube.com/watch?v=D4zqigCb8co&list=PL0oFI08O71gKEXITQ7OG2SCCXkrtid7Fq)

   - 임승현: [ML Book](https://github.com/jeonggunlee/MichinLearning/blob/master/Machine-Learning.pdf)
   
   - 임병준: 실습시 GPU 사용을 통해 빠른 learning을 하고 싶다면 --> [CLICK](https://github.com/jeonggunlee/MichinLearning/blob/master/tensorflow-gpu%20%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0.txt)
   
   - [데이터 사이언티스트 인터뷰 질문 모음](https://zzsza.github.io/data/2018/02/17/datascience-interivew-questions/)
   
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

**질문1) pooling을 쓰는 이유?**

   - Overfitting 을 방지!
   -> 이미지를 계속 필터로 만들다보면 특징의 수가 계속계속 기하 급수적으로 증가하기 때문에 overfitting의 위험이 있습니다.
       그렇기 때문에 중간에 pooling을 해준다면 개수가 적절하게 유지되어서 overfitting을 최대한 방지한다.
       참고사이트 : [링크](https://mc.ai/cnn%EC%97%90%EC%84%9C-pooling%EC%9D%B4%EB%9E%80/)

**질문 2) Max pooling을 왜 쓰는 건가?**
   
> [재민 코멘트] 일단 pooling이란 *계산 복잡도를 줄이기위해서* 사용합니다. 그렇다면 평균(average)와 최대값(max value)중에 어울리는 단어는 무엇일까요? 일반적으로 복잡한 것을 간단하게 만들기 위해서 숫자들에게 구분을 지어야 한다면 당연하게 max와 잘 어울린다고 생각하게 됩니다.  그러나 둘중 어느것이 좋다고 정확히 말할 수는 없습니다. 왜냐하면 max pooling은 중요한 부분(가장자리)을 추출하는데 특화(몇가지중 숫자 1개만 선택) 되어있고 average pooling은 부드럽고 유연한 추출을 하는데 특화(모두를 평균내어서 선택)되어 있기 때문입니다. 즉, *case에 따라 다르다는 것*입니다. 그러나 저희는 보통 이미지를 구분하는데 일반적으로 극단적인 특징을 요구한다고 합니다. 그렇기 때문에 max pooling을 사용하는 것이 아닐까요?? 결론적으로 average 보다 보편화된 max가 이유가 아닐까요?

[링크](https://www.quora.com/What-is-the-benefit-of-using-average-pooling-rather-than-max-pooling) <- 여기에 max 와 average의 차이를 보여주는 이미지가 있습니다. 그리고 여기서 참고했습니다.

질문 3) CNN이 왜 좋지 ? [링크](http://aikorea.org/cs231n/convolutional-networks/)

>컨볼루셔널 레이어 (이하 CONV) 

>CONV 레이어는 ConvNet을 이루는 핵심 요소이다. CONV 레이어의 출력은 3차원으로 정렬된 뉴런들로 해석될 수 있다. 이제부터는 뉴런들의 연결성 (connectivity), 그들의 공간상의 배치, 그리고 모수 공유(parameter sharing) 에 대해 알아보자.

>

>개요 및 직관적인 설명. CONV 레이어의 모수(parameter)들은 일련의 학습가능한 필터들로 이뤄져 있다. 각 필터는 가로/세로 차원으로는 작지만 깊이 (depth) 차원으로는 전체 깊이를 아우른다. 포워드 패스 (forward pass) 때에는 각 필터를 입력 볼륨의 가로/세로 차원으로 슬라이딩 시키며 (정확히는 convolve 시키며) 2차원의 액티베이션 맵 (activation map)을 생성한다. 필터를 입력 위로 슬라이딩 시킬 때, 필터와 입력의 요소들 사이의 내적 연산 (dot product)이 이뤄진다. 직관적으로 설명하면, 이 신경망은 입력의 특정 위치의 특정 패턴에 대해 반응하는 (activate) 필터를 학습한다. 이런 액티베이션 맵 (activation map)을 깊이 (depth) 차원을 따라 쌓은 것이 곧 출력 볼륨이 된다. 그러므로 출력 볼륨의 각 요소들은 입력의 작은 영역만을 취급하고, 같은 액티베이션 맵 내의 뉴런들은 같은 모수들을 공유한다 (같은 필터를 적용한 결과이므로). 이제 이 과정에 대해 좀 더 깊이 파헤쳐보자.

>

>로컬 연결성 (Local connectivity). 이미지와 같은 고차원 입력을 다룰 때에는, 현재 레이어의 한 뉴런을 이전 볼륨의 모든 뉴런들과 연결하는 것이 비 실용적이다. 대신에 우리는 레이어의 각 뉴런을 입력 볼륨의 로컬한 영역(local region)에만 연결할 것이다. 이 영역은 리셉티브 필드 (receptive field)라고 불리는 초모수 (hyperparameter) 이다. 깊이 차원 측면에서는 항상 입력 볼륨의 총 깊이를 다룬다 (가로/세로는 작은 영역을 보지만 깊이는 전체를 본다는 뜻). 공간적 차원 (가로/세로)와 깊이 차원을 다루는 방식이 다르다는 걸 기억하자.


질문 4) 필터의 사이즈는 어떻게 잡으면 좋을까 ? 크게 작게 ????

**2018년 10월 1일** : **Recurrent Neural Networks**

특별한 질문은 업속, 향후 모임 진행 방향 토의! : 개별 연구 진행!

**2018년 10월 4일** : 개별 관심/연구 사항 토의 미팅

    - 임병준: Gradient Descent 방법 개별연구
    - 이민정: Self Review
    - 임승현: Review
    - 정재민: Crawled data analysis
    - 이종학: Machine Learning Math.
    
    

*  *  *
### 참여자 리스트입니다.
- 소프트웨어 융합 대학 교수 이정근 [http://www.onchip.net](http://www.onchip.net)
- 컴퓨터공학과 대학원 Nguyen Van Toan 박사
- 컴퓨터공학과 대학원 김용휘 (석사과정)
- 소프트웨어 융합 대학 학부생: 임병준, 임승현, 이종학, 정재민, 김민정


