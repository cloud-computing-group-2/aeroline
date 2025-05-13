from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date
from faker import Faker
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# URL de conexión
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Configuración de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelos locales mínimos
class Pasajero(Base):
    __tablename__ = "pasajeros"

    id_pasajero = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(255))
    sexo = Column(String(50))
    fecha_nacimiento = Column(Date)
    email = Column(String(255), unique=True)
    telefono = Column(String(50))

class Compra(Base):
    __tablename__ = "compras"

    id_historial = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    asiento = Column(String(50))
    id_pasajero = Column(Integer)
    id_vuelo = Column(Integer)

# Inicializar Faker
faker = Faker()

def generar_pasajeros_y_compras_ordenado(num_registros: int):
    db: Session = SessionLocal()

    for i in range(1, num_registros + 1):
        pasajero = Pasajero(
            id_pasajero=i,
            nombre_completo=faker.name(),
            sexo=random.choice(["Masculino", "Femenino"]),
            fecha_nacimiento=faker.date_of_birth(minimum_age=18, maximum_age=80),
            email=faker.unique.email(),
            telefono=faker.phone_number()
        )
        db.add(pasajero)

        compra = Compra(
            fecha=faker.date_between(start_date="-1y", end_date="today"),
            asiento=f"{random.randint(1, 30)}{random.choice(['A','B','C','D','E','F'])}",
            id_pasajero=i,
            id_vuelo=i  # ID de vuelo también ordenado igual que el pasajero
        )
        db.add(compra)

        if i % 500 == 0:
            db.commit()

    db.commit()
    db.close()
    print(f"Se generaron {num_registros} pasajeros y compras de forma ordenada exitosamente.")

if __name__ == "__main__":
    generar_pasajeros_y_compras_ordenado(20000)
