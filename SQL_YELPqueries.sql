--SQLite
--query1. null values


SELECT COUNT(id)
        ,COUNT(name)
        ,COUNT(review_count)
        ,COUNT(yelping_since)
        ,COUNT(useful)
        ,COUNT(funny)
        ,COUNT(cool)
        ,COUNT(fans)
        ,COUNT(average_stars)
        ,COUNT(compliment_hot)
        ,COUNT(compliment_more)
        ,COUNT(compliment_profile)
        ,COUNT(compliment_cute)
        ,COUNT(compliment_list)
        ,COUNT(compliment_note)
        ,COUNT(compliment_plain)
        ,COUNT(compliment_cool)
        ,COUNT(compliment_funny)
        ,COUNT(compliment_writer)
        ,COUNT(compliment_photos)
FROM user
WHERE id IS NULL
        OR name IS NULL
				OR review_count IS NULL
				OR yelping_since IS NULL
				OR useful IS NULL
				OR funny IS NULL
				OR cool IS NULL
				OR fans IS NULL
				OR average_stars IS NULL
				OR compliment_hot IS NULL
				OR compliment_more IS NULL
				OR compliment_profile IS NULL
				OR compliment_cute IS NULL
				OR compliment_list IS NULL
				OR compliment_note IS NULL
				OR compliment_plain IS NULL
				OR compliment_cool IS NULL
				OR compliment_funny IS NULL
				OR compliment_writer IS NULL
				OR compliment_photos IS NULL
;



--query2. most reviewed cities

SELECT city
			,SUM(review_count) AS review_count_total
FROM business
GROUP BY city
ORDER BY review_count_total DESC
;



--query3. star distribution in city-Avon

SELECT stars AS star_rating
        ,COUNT(id) AS count
FROM business
WHERE city IS 'Avon'
GROUP BY stars
;


--query4. top 3 users by number of reviews

	SELECT name
	        ,id
	        ,review_count
	FROM user
	ORDER BY review_count DESC
	LIMIT 3
;


--query5. correlation between review count and fan count


SELECT AVG( (review_count - avg_x) * (fans - avg_y) )*AVG( (review_count - avg_x) * (fans - avg_y) )/(var_x*var_y) AS R2
FROM user, (SELECT avg_x
      ,avg_y
      ,AVG((review_count - avg_x)*(review_count - avg_x)) AS var_x
      ,AVG((fans - avg_y)*(fans - avg_y)) AS var_y
      FROM user,
					(SELECT AVG(review_count) AS avg_x
          		,AVG(fans) AS avg_y
          	FROM user)
  )
;


--query6. more 'love' or 'hate' in text-based reviews

SELECT 'love' AS word
	        ,COUNT(text) AS count
FROM review
WHERE text LIKE '%love%'
UNION
SELECT 'hate' as word
        ,COUNT(text) AS count
FROM review
WHERE text LIKE '%hate%'
;


--query8. users with the most fans


SELECT id
        ,name
        ,fans
FROM user
ORDER BY fans DESC
LIMIT 10
;

--query9. restaurants in Mississauga + group star rate + reformatting hours from 'Monday|12:00-6:00' to 'Mon' AND '12:00-6:00'

SELECT is_open
        ,name
        ,star_rating
        ,review_count
        ,day
        ,CASE -- remove extra characters from hours str *continuation of below
                WHEN opens LIKE '|%' THEN SUBSTR(opens,2,10)
                WHEN opens LIKE 'y%' THEN SUBSTR(opens,3,10)
                ELSE opens
        END AS hours
FROM (SELECT b.is_open
        ,b.name
        ,CASE -- convert star ratings to a high/low binary
	        WHEN b.stars < 4 AND b.stars >= 2 THEN 'LOW'
		WHEN b.stars >= 4 THEN 'HIGH'
	END AS star_rating
        ,b.review_count
        ,SUBSTR(hours,1,3) AS day --capture day of the week from hours
        ,SUBSTR(hours,-11,11) AS opens --remove day of the week from hours, needs more processing *see above
        ,h.hours
FROM (business AS b --join tables business, category, and hours
LEFT JOIN category AS c
        ON b.id = c.business_id)
                LEFT JOIN hours AS h
                        ON c.business_id = h.business_id
WHERE c.category IS 'Restaurants' --filter results for specific city and category
        AND city IS 'Mississauga'
        AND b.is_open <> 0 -- remove records with null vlaues
        AND star_rating IS NOT NULL
        AND hours IS NOT NULL
)
;

-- Results:
-- is_open | name                         | star_rating | review_count | day | hours       |
-- +---------+------------------------------+-------------+--------------+-----+-------------+
-- |       1 | The Erin Mills Pump & Patio  | LOW         |           27 | Mon | 11:00-0:00  |
-- |       1 | The Erin Mills Pump & Patio  | LOW         |           27 | Tue | 11:00-0:00  |
-- |       1 | The Erin Mills Pump & Patio  | LOW         |           27 | Fri | 11:00-1:00  |
-- |       1 | The Erin Mills Pump & Patio  | LOW         |           27 | Wed | 11:00-0:00  |
-- |       1 | The Erin Mills Pump & Patio  | LOW         |           27 | Thu | 11:00-1:00  |
-- |       1 | The Erin Mills Pump & Patio  | LOW         |           27 | Sun | 10:00-11:00 |
-- |       1 | The Erin Mills Pump & Patio  | LOW         |           27 | Sat | 10:00-1:00  |
-- |       1 | Hermanos Mexican Grill       | HIGH        |           69 | Mon | 11:30-20:00 |
-- |       1 | Hermanos Mexican Grill       | HIGH        |           69 | Tue | 11:30-20:00 |
-- |       1 | Hermanos Mexican Grill       | HIGH        |           69 | Fri | 11:30-21:00 |
-- |       1 | Hermanos Mexican Grill       | HIGH        |           69 | Wed | 11:30-20:00 |
-- |       1 | Hermanos Mexican Grill       | HIGH        |           69 | Thu | 11:30-20:00 |
-- |       1 | Hermanos Mexican Grill       | HIGH        |           69 | Sun | 12:00-20:00 |
-- |       1 | Hermanos Mexican Grill       | HIGH        |           69 | Sat | 12:00-21:00 |
-- |       1 | Masamune Japanese Restaurant | HIGH        |           61 | Mon | 16:00-22:00 |
-- |       1 | Masamune Japanese Restaurant | HIGH        |           61 | Tue | 16:00-22:00 |
-- |       1 | Masamune Japanese Restaurant | HIGH        |           61 | Fri | 16:00-22:00 |
-- |       1 | Masamune Japanese Restaurant | HIGH        |           61 | Wed | 16:00-22:00 |
-- |       1 | Masamune Japanese Restaurant | HIGH        |           61 | Thu | 16:00-22:00 |
-- |       1 | Masamune Japanese Restaurant | HIGH        |           61 | Sat | 12:00-22:00 |
-- |       1 | P & J Hamburgers Inn         | LOW         |            3 | Mon | 9:00-21:00  |
-- |       1 | P & J Hamburgers Inn         | LOW         |            3 | Tue | 9:00-21:00  |
-- |       1 | P & J Hamburgers Inn         | LOW         |            3 | Fri | 9:00-21:00  |
-- |       1 | P & J Hamburgers Inn         | LOW         |            3 | Wed | 9:00-21:00  |
-- |       1 | P & J Hamburgers Inn         | LOW         |            3 | Thu | 9:00-21:00  |
