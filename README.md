1. Create an empty schema.

2. Execute the script `OMOP CDM sql server ddl.txt` to create the tables and fields.

3. Load your data into the schema.

4. Execute the script `OMOP CDM sql server indexes.txt` to add the minimum set of indices and primary keys we recommend.


Database setting => create my_setting in patient_statistics directory and fill database info.


csv 데이터는 pgadmin 4 UI tool을 사용하여 Import 했습니다.

1. python manage.py migrate
2. python manage.py runserver


사용 언어 : Python
프레임워크: Django (restful framework), Bootstrap, ajax ..
DB : PostgresQL
