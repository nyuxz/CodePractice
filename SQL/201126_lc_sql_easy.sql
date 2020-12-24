##################################################
# 176. Second Highest Salary 
select
    (select distinct Salary
    from Employee
    order by Salary DESC
    limit 1 offset 1) as SecondHighestSalary


##################################################
# 175. Combine Two Tables
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId


##################################################
# 181. Employees Earning More Than Their Managers
select a.Name as Employee
from Employee as a, Employee as b
where a.ManagerId = b.Id and a.Salary > b.Salary


##################################################
# 196. Delete Duplicate Emails
delete p2
from Person p1, Person p2
where p1.Email = p2.Email and p1.Id < p2.Id


##################################################
# 627. Swap Salary
UPDATE salary SET sex = IF(sex='m', 'f', 'm')


##################################################
# 1517. Find Users With Valid E-Mails
select * from Users
where mail regexp '^[a-zA-Z]+[a-zA-Z0-9_\\./\\-]*@leetcode\\.com$'
order by user_id


##################################################
# 1173. Immediate Food Delivery I
select round(sum(order_date=customer_pref_delivery_date) /count(*) ,4)*100 as immediate_percentage
from Delivery

select round(sum(case when order_date=customer_pref_delivery_date then 1 else 0 end) /count(*), 4)*100
as immediate_percentage
from Delivery

select 
    round(
        (select count(*) from Delivery where order_date=customer_pref_delivery_date) /
        (select count(*) from Delivery), 4
    ) * 100
as immediate_percentage


##################################################
# 610. Triangle Judgement
select x,y,z,
    case
        when x + y > z and x + z > y and y + z > x then 'Yes'
        else 'No'
    end as 'triangle'
from triangle

select x, y, z, if(x+y>z and x+z>y and y+z>x, 'Yes', 'No') as triangle 
from triangle


##################################################
# 1435. Create a Session Bar Chart
select '[0-5>' as bin, count(1) as total
from Sessions
where duration>=0 and duration < 300
union
select '[5-10>' as bin, count(1) as total
from Sessions
where duration>=300 and duration < 600
union
select '[10-15>' as bin, count(1) as total
from Sessions
where duration>=600 and duration < 900
union
select '15 or more' as bin, count(1) as total
from Sessions
where duration >= 900


##################################################
# 182. Duplicate Emails
select distinct(p.Email)
from Person p, Person p1
where (p.Id<>p1.Id and p.Email=p1.Email)


select distinct(p.Email)
from Person p
group by p.Email
having count(p.Email)>1


##################################################
# 597. Friend Requests I: Overall Acceptance Rate
select round(count(distinct requester_id, accepter_id) / count(distinct sender_id, send_to_id), 2) as accept_rate
from FriendRequest, RequestAccepted

select round(ifnull(
    (select count(*) from (select distinct requester_id, accepter_id from RequestAccepted) as A) / 
    (select count(*) from (select distinct sender_id, send_to_id from FriendRequest) as B), 
    0), 2) as accept_rate


##################################################
# 1587. Bank Account Summary II
select a.name, sum(b.amount) as balance 
from Users as a
join Transactions as b
on a.account = b.account
group by a.account 
having balance > 10000

##################################################
# 1084. Sales Analysis III
select s.product_id, p.product_name
from Sales as s 
join Product as p
on s.product_id = p.product_id
group by s.product_id
having min(s.sale_date) >= '2019-01-01' and max(s.sale_date) <= '2019-03-31'

##################################################
# 1141. User Activity for the Past 30 Days I
select activity_date as day, count(distinct user_id) as active_users
from Activity
where activity_date between date('2019-6-28') and date('2019-7-27')
group by activity_date

##################################################
# 512. Game Play Analysis II
select distinct player_id, device_id
from Activity
where (player_id, event_date) in (
    select player_id, min(event_date)
    from Activity
    group by player_id)


##################################################
# 620. Not Boring Movies
select id, movie, description, rating
from cinema
where description not like '%boring%' and (id % 2)=1
order by rating DESC

##################################################
# 1142. User Activity for the Past 30 Days II
select ifnull(round(count(distinct session_id) / count(distinct user_id), 2), 0) as average_sessions_per_user
from Activity
where datediff('2019-07-27', activity_date) < 30

##################################################
# 1327. List the Products Ordered in a Period
select product_name, sum(unit) as unit
from Products as p
inner join Orders as o on p.product_id = o.product_id
#where left(order_date, 7) = "2020-02"
where o.order_date between '2020-02-01' and '2020-02-29'
group by p.product_id
having sum(unit)>=100


##################################################
# 1350. Students With Invalid Departments
select s.id, s.name 
from Students as s 
left join Departments as d on s.department_id = d.id
where isnull(d.id)

select distinct id, name
from Students
where department_id not in (
    select id
    from Departments
)

##################################################
# 1251. Average Selling Price
select p.product_id, round(sum(p.price * u.units)/sum(u.units), 2) as average_price
from Prices as p
inner join UnitsSold as u 
on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date
group by product_id


##################################################
# 1083. Sales Analysis II
# return a list of values after groupby
select distinct buyer_id
from Sales
left join Product on Product.product_id = Sales.product_id
group by buyer_id
having group_concat(product_name) = 'S8'

select s.buyer_id 
from sales s 
join product p 
on s.product_id = p.product_id
group by s.buyer_id
having sum(p.product_name = 'S8') > 0 and sum(p.product_name = 'iPhone') = 0

##################################################
# 584. Find Customer Referee
select name 
from customer
where referee_id <> 2 or referee_id is null


##################################################
# 586. Customer Placing the Largest Number of Orders
select distinct customer_number
from orders
group by customer_number
order by count(1) desc limit 1
# order by count(1) desc limit 1 # slower

##################################################
# 1068. Product Sales Analysis I
select p.product_name, s.year, s.price
from Sales as s
inner join Product as p on s.product_id = p.product_id


##################################################
# 1543. Fix Product Name Format
select product_name, sale_date, count(1) as total
from
(
    select 
        lcase(trim(product_name)) as product_name,
        date_format(sale_date,'%Y-%m') sale_date
    from Sales
) as new_sales
group by product_name, sale_date
order by product_name, sale_date

##################################################
# 595. Big Countries
select name, population, area
from World
where area > 3000000 or population > 25000000


SELECT name, population, area
FROM World
WHERE area > 3000000
UNION
SELECT name, population, area
FROM World
WHERE population > 25000000

##################################################
# 1280. Students and Examinations
select a.student_id, a.student_name, b.subject_name, count(e.subject_name) as attended_exams
from Students a cross join Subjects b
left join Examinations e on a.student_id = e.student_id and b.subject_name = e.subject_name
group by a.student_id, b.subject_name
order by a.student_id, b.subject_name


##################################################
# 1484. Group Sold Products By The Date
select sell_date, count(distinct product) as num_sold, group_concat(distinct product) as products
from Activities
group by sell_date


##################################################
# 603. Consecutive Available Seats
select distinct c1.seat_id from cinema c1,
cinema c2 
where (c1.seat_id+1=c2.seat_id or c1.seat_id-1=c2.seat_id)
and (c1.free=1 and c2.free=1)

##################################################
# 613. Shortest Distance in a Line
select min(abs(p2.x-p1.x)) as shortest
from point as p1, point as p2 
where p1.x <> p2.x

##################################################
# 1303. Find the Team Size
select e.employee_id, t.team_size
from Employee as e
inner join (select team_id, count(1) as team_size
            from Employee 
            group by team_id) as t 
on e.team_id = t.team_id

##################################################
# 596. Classes More Than 5 Students
select t.class
from (select class, count(distinct student) as cnt
from courses
group by class
having cnt >=5 ) as t

##################################################
# 1667. Fix Names in a Table
# SUBSTRING(string, start, length)
SELECT user_id, 
       Concat(Upper(Substring(name, 1, 1)), Lower(Substring(name, 2))) AS name 
FROM   users 
ORDER  BY user_id 

##################################################
# 1407. Top Travellers
select u.name, ifnull(sum(distance), 0) as travelled_distance
from Users as u
left join Rides as r 
on u.id = r.user_id
group by u.id
order by travelled_distance desc, u.name asc


##################################################
# 1378. Replace Employee ID With The Unique Identifier
' Left join, benchmark at from'
select euni.unique_id, e.name
from Employees as e
left join EmployeeUNI as euni
on e.id = euni.id

##################################################
# 1294. Weather Type in Each Country
select country_name, 
case 
    when avg(weather_state) <= 15 then 'Cold'
    when avg (weather_state)>= 25 then 'Hot'
    else 'Warm'
end as weather_type
from Countries as c
join Weather as w on c.country_id = w.country_id
where date_format(day,'%Y-%m') = '2019-11'
group by c.country_id


##################################################
# 1571. Warehouse Manager
select w.name as warehouse_name, sum(p.Width * p.Length * p.Height * w.units) as volume
from Warehouse as w
inner join Products as p
on w.product_id = p.product_id
group by w.name

##################################################
# 1661. Average Time of Process per Machine
# group by the first column
# group by 1 
# order by 1

WITH times 
     AS (SELECT machine_id, 
                Sum(If(activity_type = 'end', timestamp, 0)) - Sum( 
                If(activity_type = 'start', timestamp, 0)) as total_process_time, 
                Count(DISTINCT process_id) as number_processes 
         FROM   activity 
         GROUP  BY machine_id) 
         
SELECT machine_id, 
       Round(total_process_time / number_processes, 3) AS processing_time 
FROM   times 

##################################################
# 1677. Products Worth Over Invoices
select name, sum(rest) as rest, sum(paid) as paid, sum(canceled) as canceled, sum(refunded) as refunded
from product
join invoice on Invoice.product_id = Product.product_id
group by name
order by name

##################################################
# 1633. Percentage of Users Attended a Contest
select contest_id, round(count(distinct user_id) / (select count(distinct user_id) from Users)*100, 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id 

##################################################
# 1607. Sellers With No Sales
# Use sum, not use count

select seller_name 
from Orders
right join Seller
on Seller.seller_id = Orders.seller_id
group by seller_name
having ifnull(sum(year(sale_date)=2020),0)=0
order by seller_name

##################################################
# 1581. Customer Who Visited but Did Not Make Any Transactions
select customer_id, count(1) as count_no_trans
from Visits as v
left join Transactions as t on v.visit_id = t.visit_id
where t.transaction_id is null
group by customer_id


##################################################
# 1565. Unique Orders and Customers Per Month
# for the order format function, %m is numerical month, %M is string month

select date_format(order_date, '%Y-%m') as month,
count(invoice) as order_count,
count(distinct customer_id) as customer_count
from Orders
where invoice > 20
group by year(order_date), month(order_date)


##################################################
# 1511. Customer Order Frequency

select customer_id, name
from customers
where customer_id in
(
select t.customer_id from 
(select o.customer_id
from Orders as o
left join Product as p on o.product_id = p.product_id
left join Customers as c on o.customer_id = c.customer_id
where month(o.order_date)=6
group by o.customer_id
having sum(o.quantity*p.price) >=100) as t

where t.customer_id in

(select o.customer_id
from Orders as o
left join Product as p on o.product_id = p.product_id
left join Customers as c on o.customer_id = c.customer_id
where month(o.order_date)=7
group by o.customer_id
having sum(o.quantity*p.price) >=100)
)


##################################################
# 1495. Friendly Movies Streamed Last Month




