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
Project
    | patient_statistics (Home directory)
    | setting.py > 앱과 기타 설정들입니다. Migrate 진행 전 반드시 Database 란을 my_setting.py 
    에 기입해 작성해주십시오. (my_setting.DATABASE)
        | templates
        | base.html > 모든 templates의 기본 틀입니다.
        | home html > 홈입니다. 상단 간단한 링크와 이후 기능 추가 시 필요하여 제작하였습니다.
    | patients (환자 유형별 통계 APP)
        | models.py > 데이터베이스를 담은 6가지 모델입니다. 주로 person과 visit occurrence만 사용
        하였습니다.
        | serializers.py > 데이터를 JSON으로 바꾸기 위해 사용하였습니다.
        | view.py > Template view와 JSON형태로 데이터를 Response 하는 data list view로 나누어져
        있습니다.
        | templates
            | patients_all.html > 환자 유형별 통계를 나타냅니다. 데이터를 한꺼번에 가져와 차트 바와
            표로 표현했습니다.
    | visit (방문 유형 및 환자 유형별 방문 횟수)
          | models.py, serializers.py, views.py
        | templates
          | visit_parameter.html 유형별로 나누어 각각에 대한 방문횟수를 제공하는 API 입니다. 차트
          바로 그릴 수 있지만 나누는 정보가 적어 사용하지 않고 간단히 표로 표현했습니다.