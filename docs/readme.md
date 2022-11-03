## init ##
    
    pip install fastapi "uvicorn[standard]"
    pip install sqlalchemy
    pip install alembic
    pip install virtualenv 
    pip install psycopg2-binary 


## virtual env activated ##

    source venv/bin/activate (deactivate)


## requirements.txt oluşturur ve yüklenmiş olan kütüphaneleri bu txt'ye ekler ##
    
    pip freeze > requirements.txt


## Klasör ve Dosya oluşturur ##

    mkdir src && touch src/main.py 


 ## Makefile dosyası oluşturur ve o dosya içerisinde ki keylere göre komut çalıştırır ##
   
    touch Makefile
    make run-db   


## alembic kütüphanesine ait versionların tutulduğu klasör yapısını oluşturur ##
    
    alembic init migrations


## alembic üzerinden ilk migration işlemi için dosya oluşturulur ##
  
    alembic revision -m "init"


## alembic üzerinden son versiona bakarak neler değiştiğini otomatik algılayıp yeni migration dosyası oluşturur ##
    
    alembic revision --autogenerate -m "user_add_column_age"


## alembic üzerinden en güncel migration ı anlayıp çalıştırıyor ##
    
    alembic upgrade head 


## alembic üzerinden spesifik migration ##
    
    alembic upgrade "version numarası" 


## uvicorn start ##
    uvicorn src.main:app --reload



