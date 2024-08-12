select t2.country,
       sum(t1.streaming) quantidade
  from money_makers t1 
  left JOIN artist_country_continent t2
    ON( t1.artist = t2.artist )
  group BY country
