setwd("G:\\项目\\网易云音乐评论\\文本挖掘")
csv <- read.csv("text2.csv",header=T, stringsAsFactors=F)
mystopwords<-unlist(read.table("StopWords.txt",stringsAsFactors=F))
dim(csv)
csv<-as.data.frame(csv)
head(csv)
#install.packages("tibble")
library(tibble)
d1<-csv
d2<-as.tibble(d1)
d2
library(dplyr)
library(tidyr)
library(purrr)
library(readr)
library(stringr)
group_by(d2,userID)
cleaned_text<-d2


library(tidytext)
usenet_words <- cleaned_text %>%
  unnest_tokens(word, context) %>%
  filter(str_detect(word, "[a-z']$"),
         !word %in% stop_words$word)


#Words in Newsgroups
usenet_words<-cleaned_text

usenet_words %>%
  count(context, sort = TRUE)



