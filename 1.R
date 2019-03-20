

#################数据处理
##################################################################
## 1.4读取资料库


setwd("G:\\项目\\网易云音乐评论\\文本挖掘")
csv <- read.csv("train.csv",header=T, stringsAsFactors=F)
mystopwords<-unlist(read.table("StopWords.txt",stringsAsFactors=F))

## 1.5.数据预处理（中文分词、stopword处理）


#install.packages("tm",lib="E:/R语言/R语言学习/安装包")
library(NLP,lib="G:\\R语言\\R语言学习\\安装包")
library(tm,lib="G:\\R语言\\R语言学习\\安装包")
#只有RJava配置成功了，Rwordseg安装才可能成功，前者是后者的依赖包
#install.packages("rJava",lib="E:/R语言/R语言学习/安装包")
library(rJava,lib="G:\\R语言\\R语言学习\\安装包")
#手动下载安装包Rwordseg，然后本地安装
library(Rwordseg,lib="G:\\R语言\\R语言学习\\安装包")

segmentCN('牡丹是个书写时代华章的好同志')

#(1)移除数字函数
removeNumbers = function(x) { ret = gsub("[0-9０１２３４５６７８９]","",x) }

#(2)strsplit分词函数
#中文分词，也可以考虑使用 rmmseg4j、rsmartcn 
wordsegment<- function(x) { 
  library(Rwordseg) 
  segmentCN(x)
} 

#(3)去除停止词函数 
removeStopWords = function(x,words) {     
  ret = character(0) 
  index <- 1 
  it_max <- length(x) 
  while (index <= it_max) { 
    if (length(words[words==x[index]]) <1) ret <- c(ret,x[index]) 
    index <- index +1 
  } 
  ret 
} 

#（1）移除数字
sample.words <- lapply(csv$text, removeNumbers) 
dim(as.matrix(sample.words))

#（2）中文分词
sample.words <- lapply(sample.words, wordsegment) 
dim(as.matrix(sample.words))
#sample.words[1:6]

#（3）移除停止词
#先处理中文分词，再处理 stopwords，防止全局替换丢失信息,
#下面这句运行时间较长 
sample.words <- lapply(sample.words, removeStopWords, mystopwords) 
dim(as.matrix(sample.words))

#构建语料库 
corpus = Corpus(VectorSource(sample.words)) 
meta(corpus,"cluster") <- csv$type 
unique_type <- unique(csv$type) 
corpus
#建立文档-词条矩阵 
(sample.dtm <- DocumentTermMatrix(corpus, control = list(wordLengths = c(2, Inf)))) 

inspect(removeSparseTerms(sample.dtm, 0.5))
findAssocs(sample.dtm,"無",0.4)

(d <- c("王"))
dim(sample.dtm)

inspect(DocumentTermMatrix(corpus, list(dictionary = d)))
findFreqTerms(sample.dtm, 400)
findFreqTerms(sample.dtm[8:22,],30)
findFreqTerms(sample.dtm[23:33,],30)
str(sample.dtm)
dim(sample.dtm)
as.matrix(sample.dtm)[,which(colnames(sample.dtm)=="無")]

sample.dtm[1:3,1:4]
writeCorpus(corpus)


#31个文档，4142个词条
write.csv(as.matrix(sample.dtm),"sample.dtm.csv")



################################################################
#####################





















