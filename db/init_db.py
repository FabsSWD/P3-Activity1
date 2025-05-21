from app import create_app, db
from models.models import Usuario, Libro

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    if not Usuario.query.filter_by(correo='admin@admin.com').first():
        admin = Usuario(
            nombre='admin',
            correo='admin@admin.com',
            identificacion='0000',
            rol='admin'
        )
        admin.set_password('1234')
        db.session.add(admin)

    libros_demo = [
        Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", categoria="Novela", anio=1967, sinopsis="Saga de la familia Buendía."),
        Libro(titulo="1984", autor="George Orwell", categoria="Distopía", anio=1949, sinopsis="Un clásico sobre el totalitarismo."),
        Libro(titulo="El principito", autor="Antoine de Saint-Exupéry", categoria="Fábula", anio=1943, sinopsis="Un pequeño príncipe viaja por planetas."),
    ]

    db.session.bulk_save_objects(libros_demo)
    db.session.commit()

    print("Base de datos creada con admin y libros iniciales.")
