# Name: 	Andres Rodriguez
# Course:       CPE 101
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set I
# Term:         Winter 2020


def problem_1() -> None:
	Num = input('Pick a number between 1 and 20: ')
	x = int(Num) * int(2)
	x = int(x) + int(10)
	x = int(x) / int(2)
	x = int(x) - int(Num)
	print(x)
	#Result = (int(Num)*int(2)+int(10))/int(2)-int(Num)
	#print(Result)	

def problem_2() -> None:
	Num = input('Pick a number: ')
	Num2 = input('Pick a second number: ')
	Num3 = int(Num) + int(Num2)
	Num4 = int(Num2) + Num3
	Num5 = Num4 + Num3
	Num6 = Num5 + Num4
	Num7 = Num6 + Num5
	Num8 = Num7 + Num6
	Num9 = Num8 + Num7
	Num10 = Num9 + Num8
	Final = (int(Num) + int(Num2) + Num3
		 + Num4 + Num5 + Num6 + Num7 + Num8 + Num9 + Num10)
	Final = Final / Num7
	print(Final)	


def problem_3() -> None:
	num = input('Pick a four-digit number where each digit is different: ')
	x = int(num)
	Ths = x // int(1000)
	x = x - Ths * int(1000)
	Hun = x // int(100)
	x = x - Hun * int(100)
	Ten = x // int(10)
	One = x - Ten * int(10)
	New = One * int(1000) + Hun * int(100) + Ten * int(10) + Ths
	print(x)
	print(New)
	Sub = max(int(num), New) - min(int(num), New)
	print(Sub) 
	Ths = Sub // int(1000)
	Sub = Sub - Ths * int(1000)
	Hun = Sub // int(100)
	Sub = Sub - Hun * int(100)
	Ten = Sub // int(10)
	Sub = Sub - Ten * int(10)
	Final = Ths + Hun + Ten + Sub
	Fst = Final // int(10)
	Sec = Final - Fst * int(10)
	Done = Fst + Sec
	print(Ths)
	print(Hun)
	print(Ten)
	print(Sub)
	print(Final)
	print(Done)


def problem_4() -> None:
	num = input('Pick a number between 1 and 50, not divisible by 7: ')
	x = int(num) / int(7)	
	print(x)
	one = x // int(1)
	x = x - one
	ten = x // float(.1)
	x = x - ten * float(.1)
	hun = x // float(.01)
	x = x - hun * float(.01)
	ths = x // float(.001)
	x = x - ths * float(.001)
	tths = x // float(.0001)
	x = x - tths * float(.0001)
	hths = x // float(.00001)
	x = x - hths * float(.00001)
	mil = x // float(.000001)
	Sum = ten + hun + ths + tths + hths + mil
	print(Sum)


if __name__ == "__main__":
   # problem_1()
   # problem_2()
    problem_3()
   # problem_4()
