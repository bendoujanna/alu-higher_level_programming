#!/bin/bash
# Script to list all privileges of user_0d_1 and user_0d_2

mysql -u root -p -e "
-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
"
