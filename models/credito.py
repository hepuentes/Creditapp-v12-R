from datetime import datetime
from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Credito(db.Model):
    __tablename__ = 'credito'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_vencimiento = db.Column(db.DateTime)
    fecha_pago = db.Column(db.DateTime)

    monto_total = db.Column(db.Numeric(12, 0), nullable=False)
    saldo = db.Column(db.Numeric(12, 0), nullable=False)
    numero_cuotas = db.Column(db.Integer, nullable=False)
    monto_cuota = db.Column(db.Numeric(12, 0), nullable=False)
    modalidad_pago = db.Column(db.String(20), default='mensual')  # diario, semanal, etc.

    estado = db.Column(db.String(50), default='activo')
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
