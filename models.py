from app import db

class NMS(db.Model):
    __tablename__ = 'snmptest'
    id = db.Column(db.Integer, primary_key=True)
    oid = db.Column(db.String())
    location = db.Column(db.String())
    uptime = db.Column(db.Integer())

    def __init__(self, oid, location, uptime):
        self.oid = oid
        self.location = location
        self.uptime = uptime

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'oid': self.oid,
            'location': self.location,
            'uptime': self.uptime}

class Hosttable(db.Model):
    __tablename__ = 'hosttable'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String())
    name = db.Column(db.String())
    status = db.Column(db.Integer())

    def __init__(self, ip, name, status):
        self.ip = ip
        self.name = name
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'ip': self.ip,
            'name': self.name,
            'status': self.status}
