# Basket-Analysis-Project
장바구니 데이터 분석 프로젝트

## 프로젝트 설명
  + Frequent Pattern Analysis & Association Rule Mining을 기반으로 한 장바구니 분석
  + Apriori Algorithm 사용
  + input data : Black Friday 상품 판매 데이터(The set of item ID)
  + output file format : [item_id]→[association_itemset] ,[support] ,[confidence]
    + support : 동시에 판매되는 item set에 item_id 와 association_itemset이 함께 존재할 확률
    + confidence : item_id가 판매될 때 항상 association_itemset이 같이 판매될 확률
  + 결과적으로 어떤 상품을 함께 진열해야 더 잘 팔리는지에 대한 insight을 제공

## Tech and Skill
  + python, Frequent Pattern Analysis, Apriori Algorithm
## input data
<img width="662" alt="_2021-05-16__1 14 21" src="https://user-images.githubusercontent.com/83147205/165786745-d8ed4203-5b82-4832-85a4-b57bc44e97bf.png">

첫 줄은 물건을 산 사람의 아이디, 나머지는 각 사람들이 산 물건의 아이디
## 결과 데이터
<img width="662" alt="_2021-05-16__1 15 37" src="https://user-images.githubusercontent.com/83147205/165787018-792f3185-b824-4aed-a40f-4fff8c20fdcb.png">
support과 confidence를 구해서 함께 어떤 상품들을 함께 진열해야 하는지에 대한 insight을 얻기
