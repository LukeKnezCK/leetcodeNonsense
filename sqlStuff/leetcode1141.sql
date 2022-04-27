SELECT activity_date AS day, COUNT(DISTINCT(user_id)) AS active_users FROM Activity
WHERE (TO_DAYS('2019-07-27') - TO_DAYS(activity_date) < 30 )
GROUP BY activity_date