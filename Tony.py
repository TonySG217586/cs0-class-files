HW = [100,100,100,85,65,100,100,100,0,105,105]
HWgrade = .2
HWAverage = (float(sum(HW))/11)*HWgrade
print "Average Homework score" + str(HWAverage)

Quiz = [93,87,100,100,72]
Quizgrade = .25
QuizAverage = (float(sum(Quiz))/5)*Quizgrade
print "Average Quiz score" + str(QuizAverage) 

Test = [98,92,75,80]
Testgrade = .3
TestAverage = (float(sum(Test))/4)*Testgrade
print "Average Test score" + str(TestAverage)

MidT = 85
MidTgrade = .1
MidTAverage = (float(MidT)/1)*MidTgrade
print "AverageMIdterm score" + str(MidTAverage)

Averagelist =(HWAverage, QuizAverage, TestAverage, MidTAverage)
AllAverage = sum(Averagelist)
print "Average without Final Exam =" + str(AllAverage)

ScoreforA=90
AverageScoreNeedForFinal= ScoreforA- (AllAverage)
ScoreNeedOnFinalExam= AverageScoreNeedForFinal /.15
print ScoreNeedOnFinalExam

