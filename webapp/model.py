from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class News(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        titleEs = db.Column(db.String, nullable=False)
        titleRu = db.Column(db.String, nullable=False)
        titleEn = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        fecha = db.Column(db.DateTime, nullable=False)
        shorttextEs = db.Column(db.Text, nullable=True)
        shorttextRu = db.Column(db.Text, nullable=True)
        shorttextEn = db.Column(db.Text, nullable=True)
        textEs = db.Column(db.Text, nullable=True)
        textRu = db.Column(db.Text, nullable=True)
        textEn = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return '<News {} {} {} {} {}>'.format(self.titleEs, self.url, self.fecha,self.shorttextEs,self.textEs)
