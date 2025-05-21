from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from models.models import Usuario, Libro
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    q = request.args.get('q', '').strip()
    if q:
        libros = Libro.query.filter(
            (Libro.titulo.ilike(f"%{q}%")) |
            (Libro.autor.ilike(f"%{q}%")) |
            (Libro.categoria.ilike(f"%{q}%"))
        ).all()
    else:
        libros = Libro.query.order_by(Libro.titulo).all()

    return render_template('index.html', libros=libros, query=q)

@main_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        identificacion = request.form['identificacion']

        if Usuario.query.filter_by(correo=correo).first():
            flash('El correo ya está registrado.')
            return redirect(url_for('main.registro'))

        usuario = Usuario(
            nombre=nombre,
            correo=correo,
            identificacion=identificacion
        )
        usuario.set_password(contraseña)
        db.session.add(usuario)
        db.session.commit()

        flash('Registro exitoso. Ahora puede iniciar sesión.')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        usuario = Usuario.query.filter_by(correo=correo).first()
        if usuario and usuario.check_password(contraseña):
            login_user(usuario)
            return redirect(url_for('main.index'))
        else:
            flash('Credenciales incorrectas.')

    return render_template('login.html')

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main_bp.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if not current_user.is_admin():
        flash('Acceso restringido solo para administradores.')
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        nuevo = Libro(
            titulo=request.form['titulo'],
            autor=request.form['autor'],
            categoria=request.form['categoria'],
            sinopsis=request.form['sinopsis'],
            anio=request.form['anio'],
            disponible='disponible' in request.form
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Libro creado exitosamente.')
        return redirect(url_for('main.admin'))

    libros = Libro.query.order_by(Libro.titulo).all()
    return render_template('admin.html', libros=libros)

@main_bp.route('/eliminar_libro/<int:libro_id>', methods=['POST'])
@login_required
def eliminar_libro(libro_id):
    if not current_user.is_admin():
        flash('Solo los administradores pueden eliminar libros.')
        return redirect(url_for('main.index'))

    libro = Libro.query.get_or_404(libro_id)
    db.session.delete(libro)
    db.session.commit()
    flash(f'Se eliminó el libro "{libro.titulo}".')
    return redirect(url_for('main.admin'))

@main_bp.route('/libro/<int:libro_id>')
def libro_detalle(libro_id):
    libro = Libro.query.get_or_404(libro_id)
    return render_template('libro_detalle.html', libro=libro)
