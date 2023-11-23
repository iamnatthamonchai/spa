# How to

 - Checkout Odoo 14.0 from https://github.com/odoo/odoo
 - Create virtualEnv and run 
     ```python
    pip install -r requirements.txt
     ```
 - Create folder *custom-addons* in checked out odoo folder
 - Move this project into *custom-addons* folder
 - Edit file *odoo.conf*
 - Run with command
    ```sh
    ./run-odoo.sh
    ```

# odoo.conf
```sh
[options]
db_name = <name of database>
db_host = False
db_port = False
db_user = <DB username>
db_password = <DB password>
addons_path = <Absolute path to custom-addons folder>
```
# PostGresQL
Odoo project use PostGresQL as default database (Download from https://www.postgresql.org/download/). Odoo 14.0 is tested with PostgresQL version 13.2
## Basic PostGresQL Commands
| Command | Description |
| ------- | ----------- |
| $ postgres -V postgres | Check postgresQL version |
| $ psql --u postgres | Login to Postgres Shell with *postgres* user |
| >> \? | Show list of commands |
| >> \l | List all databases |
| >> \q | Quit from postgres shell |
| >> \connect <db_name> | Using db_name (call this command before select, insert, etc.) |
| >> create user odoo with encrypted password '<password>' | Create use *odoo* with password |
| >> grant all privileges on database odoo to odoo; | Grant DB privileges to odoo user |
| >> ALTER USER odoo WITH SUPERUSER; | Make *odoo* user a Super User |

## How to reset Odoo 14  admin password
1. Run these python code to generate an encrypted password
    ```python
    >>> from passlib.context import CryptContext
    >>> setpw = CryptContext(schemes=['pbkdf2_sha512'])
    >>> setpw.encrypt('YourNewPassword')
    ```
2. Copy the encrypted password from python console
3. Go into PostGresQL shell
    ```sh
    $ psql --u postgres
    ```
4. Connect to Odoo Datbase and Run these queries
    ```sh
    >> \connect odoo;
    >> UPDATE res_users SET password='<YourCopiedHash>' WHERE id=2;
    # You can check user id with "select * from res_users;"
