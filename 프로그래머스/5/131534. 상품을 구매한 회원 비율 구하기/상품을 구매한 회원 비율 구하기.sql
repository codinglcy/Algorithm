-- 코드를 입력하세요
with users as (
    select user_id as id, count(*) over() as cnt
      from user_info
     where to_char(joined, 'YYYY') = '2021'
), sales as (
    select user_id,
           to_number(to_char(sales_date, 'YYYY')) as year,
           to_number(to_char(sales_date, 'MM')) as month
      from online_sale
)
select sales.year,
       sales.month,
       count(distinct sales.user_id) as puchased_users,
       round(count(distinct sales.user_id)/users.cnt, 1) as puchased_ratio
  from users, sales
 where sales.user_id in users.id
group by sales.year, sales.month, users.cnt
order by sales.year, sales.month