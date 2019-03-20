setwd("G:\\项目\\网易云音乐评论")
install.packages("xlsx",lib="G:\\R语言\\R语言学习\\安装包")
library(xlsx,lib="G:\\R语言\\R语言学习\\安装包") 
userInfo=read.csv("userProvinceInfo.csv")
code=read.table("clipboard",header = TRUE)

pro=matrix(0,nrow(userInfo),1)
for(i in 3:36){
  pro[i-2,1]=as.matrix(code[which(userInfo[i,2]==code[,1]),2])[1,1]
}
pro=pro[-c(35,36,37),]
data=cbind(userInfo[-c(35,36,37),1],pro)
colnames(data)<-c("userCounts","Province")
write.xlsx(x = data, file = "data.xlsx",
           sheetName = "data", row.names = FALSE)


