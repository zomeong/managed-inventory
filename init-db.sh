#!/bin/bash
mariadb -u"${MARIADB_ID}" -p"${MARIADB_PASSWORD}" -e "CREATE DATABASE IF NOT EXISTS \`${DB_NAME}\`;"