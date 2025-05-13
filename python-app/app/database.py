import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from faker import Faker

# Cargar las variables de entorno
load_dotenv()

# Parámetros de la base de datos desde el archivo .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_PASSWORD_ESCAPED = quote_plus(DB_PASSWORD)

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD_ESCAPED}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Crear el tipo base para las clases ORM
Base = declarative_base()

# Crear el objeto sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Faker
fake = Faker()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)

def fake_pasajero():
    return {
        "nombre_completo": fake.name(),
        "sexo": fake.random_element(["M", "F"]),
        "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
        "email": fake.email(),
        "telefono": fake.phone_number()
    }

def fake_compras():
    return {
        "id_historial": fake.random_int(min=1, max=1000),
        "fecha": fake.date(),
        "asiento": fake.random_element(elements=("1A", "2B", "3C")),
        "id_pasajero": fake.random_int(min=1, max=100), # FIXME: add constraint in range of existing users
        "id_vuelo": fake.random_int(min=1, max=100)
    }

def fake_membresias():
    return {
        "id_membresia": fake.random_int(min=1, max=1000),
        "tipo": fake.random_element(elements=("Gold", "Silver", "Bronze")),
        "fecha_inicio": fake.date(),
        "fecha_fin": fake.date(),
        "id_pasajero": fake.random_int(min=1, max=100)
    }

def faking_db(count = 10):
    [fake_pasajero() for _ in range(count)]
    [fake_compras() for _ in range(count)]
    [fake_membresias() for _ in range(count)]
    pass
