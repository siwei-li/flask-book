from api_app import db

from sqlalchemy.dialects.mysql import FLOAT

class User(db.Model):
    """
    模型，将映射到数据库表中
    """
    __tablename__ = 'users'

    # 主键ID
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(20), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(16), nullable=False)

    def to_dict(self):
        res_dict = {
            'id': self.id,
            'mobile': self.mobile,
            'nickname': self.nickname,
        }
        return res_dict


class Book(db.Model):
    """
    模型，将映射到数据库表中
    """
    __tablename__ = 'books'

    # 主键ID
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=True)
    price = db.Column(FLOAT(precision=7, scale=2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.Enum("0","1"), default="1")

    def to_dict(self):
        res_dict = {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
        }
        return res_dict



