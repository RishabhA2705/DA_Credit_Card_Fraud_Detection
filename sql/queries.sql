
use credit_fraud;

-- 1. Total transactions
select count(*) as total_transactions from transactions;

-- 2. Fraud vs Legit transactions
select class , count(*) as count from transactions group by class;

-- 3. Fraud percentage
select (sum(case when class = 1 then 1 else 0 end)/count(*))* 100 as fraud_percentage from transactions;

-- 4. Average transaction amount (fraud vs legit)
select class , round(avg(amount),2) as avg_amount from transactions group by class;

-- 5. Top 10 highest fraud amounts
select amount , time from transactions where class = 1 order by amount desc limit 10 ;

-- 6. Fraud distribution by hour
select floor(time/3600) as hour , count(*) as fraud_count from transactions where class = 1 group by hour order by hour; 

--7. Average amount by hour (fraud vs legit)
select floor(time/3600) as hour , class , round(avg(amount),2) as avg_amount from transactions group by hour , class order by hour , class ; 