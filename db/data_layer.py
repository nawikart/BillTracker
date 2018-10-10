from db.base import DbManager
from db.models import System_app
from pprint import pprint


db = DbManager()

def create_data(data_obj):
    try:
        data = System_app()
        data.parse_json(data_obj)
        return db.save(data)
    except:
        pass

    return None

def read_data(id):
    try:
        data_obj = db.open().query(System_app).filter(System_app.id == id).one()
        data = {
            'name': data_obj.name,
            'api_key': data_obj.api_key,
            'type': data_obj.type,
            'status': data_obj.status,
            'ip': data_obj.ip
        }
        return data

    except:
        pass

    return None        


# def read_data_all():
#     return db.open().query(System_app).all()


def update_data(id, data_obj):
    try:
        data = db.open().query(System_app).filter(System_app.id == id).one()
        data.parse_json(data_obj)
        return db.save(data)
    except:
        pass
    
    return None

def delete_data(id):
    try:
        data = db.open().query(System_app).filter(System_app.id == id).one()
        db.delete(data)
        return True
    except:
        pass
    
    return False

 