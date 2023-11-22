from flask import Blueprint, render_template

import mysql.connector
from app.db_config import db_config

catalogo_bp = Blueprint('catalogo', __name__)

@catalogo_bp.route('/catalogo') 
def catalogo():
    cnx = mysql.connector.connect(**db_config)
    try:
        with cnx.cursor() as cursor:
            sql = "select * from usuario WHERE FK_IdRol = 2"
            cursor.execute(sql)
            datosUser = cursor.fetchall()
            cursor.commit()
            cursor.close()

    except Exception as ex:
        print(ex)



    return render_template("catalogo.html", datos =datosUser)