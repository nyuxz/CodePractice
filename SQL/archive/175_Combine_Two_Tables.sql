# 175. Combine Two Tables

select FirstName, LastName, City, State
from Person
left join Address
on Person.PersonId = Address.PersonId

'''
P.s.
1. LEFT JOIN returns all rows from the left table, even if there are no matches in the right table.
2. If right table having no matching value,  then retuen with NULL
3. In some databases LEFT JOIN is called LEFT OUTER JOIN.
'''