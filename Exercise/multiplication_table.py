# -*- coding: utf-8 -*- 
#! /bin/zsh


n = input("단 수를 입력해주세요.(종료를 원하시면 0)")
while n!=0 :
    for i in range(9):
        print("%d X %d = %d"%(n,i+1,n*(i+1)))
    n = input("단 수를 입력해주세요.(종료를 원하시면 0)")
