# python study

## 기본 문법

### 변수

```
	a = "A"
```

### 반복문

break : loop 문 종료
continue : 다음 loop 문으로
pass : 아무것도 하지 않음

```
	for 변수 in range(카운트):
		로직 구현
	
	for 변수 in 배열 혹은 리스트, 튜플, 딕셔너리:
		로직 구현	
	
```

### 조건문 
```
	if x == "1":
		로직 구현
	elif x == "2":
		다음 로직
	else:
		마지막 로직
```

### 함수
파라미터에는 기본 default 값 삽입 가능
(*변수명) 을 사용하여 가변인자 형태로 받을 수 있음.

(**변수명) 형태를 사용하면 key value 형태로 받을 수 있음.

return (반환값1, 반환값2) 을 통해서 두개이상의 값을 반환 가능

```
	def 함수명(파라미터):
		함수 로직
		
	# 가변인자 
	def cheeseshop(kind, *arguments, **keywords):
   		for arg in arguments:
       	print(arg)
   		for kw in keywords:
      		print(kw, ":", keywords[kw])
      		
    # 가변인자 함수 사용 
    cheeseshop("Limburger", "It's very runny, sir.", shopkeeper="Michael Palin", client="John Cleese")
           
    # 두개 이상의 반환값
    def cal_upper_lower(price):
        offset = price * 0.3
        upper = price + offset
        lower = price - offset
        return (upper, lower)
    
    # 위의 함수 사용
    (upper, lower) = cal_upper_lower(10000)
   
```

### 모듈 사용하기 

```
	import 모듈명
	import 모듈명 as 변수로쓸모듈명
	from 모듈명 import 함수
```