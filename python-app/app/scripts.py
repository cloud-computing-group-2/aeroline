from faker import Faker
from app.models import Pasajero, Compra, Membresia
from app.database import engine, Base, SessionLocal, get_db

# Faker
fake = Faker()
emails_generados = set()  # Almacena correos únicos

def init_db():
    Base.metadata.create_all(bind=engine)

def fake_pasajero(db):
    email = fake.email()
    while email in emails_generados or db.query(Pasajero).filter_by(email=email).first() or len(email) > 32:
        email = fake.email()
    emails_generados.add(email)

    return {
        "nombre_completo": fake.name(),
        "sexo": fake.random_element(["M", "F"]),
        "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
        "email": email,
        "telefono": fake.phone_number()
    }


def fake_compras(id_pasajero):
    return {
        "fecha": fake.date(),
        "asiento": fake.random_element(elements=("1A", "2B", "3C")),
        "id_pasajero": id_pasajero,
        "id_vuelo": fake.random_int(min=1, max=20000)
    }

def fake_membresias(id_pasajero):
    return {
        "tipo": fake.random_element(elements=("Gold", "Silver", "Bronze")),
        "fecha_exploracion": fake.date(),
        "id_pasajero": id_pasajero,
    }

def faking_db(count=10):
    db = SessionLocal()
    try:
        # Crear y agregar pasajeros
        pasajeros = []
        for _ in range(count):
            pasajero_data = fake_pasajero(db)
            pasajero = Pasajero(**pasajero_data)
            db.add(pasajero)
            pasajeros.append(pasajero)
        db.commit()  # Confirmar para obtener IDs generados

        # Crear y agregar compras
        for pasajero in pasajeros:
            compra_data = fake_compras(pasajero.id_pasajero)
            compra = Compra(**compra_data)
            db.add(compra)

        # Crear y agregar membresías
        for pasajero in pasajeros:
            membresia_data = fake_membresias(pasajero.id_pasajero)
            membresia = Membresia(**membresia_data)
            db.add(membresia)

        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()