from flask import Blueprint, jsonify, request  
from connectionBD import connection_mysql 

app1 = Blueprint('getUsers', __name__)

#Metodo GET para crear usuarios
@app1.route('/usuarios', methods=['GET'])
def listUsers() :
    connection = connection_mysql()

    with connection.cursor() as cursor : 

        sql = 'SELECT Usu_Id, Usu_Nombre, Usu_Telefono, Usu_Correo FROM usuarios'
        cursor.execute(sql)

        result = cursor.fetchall()
        
        return jsonify({
            'data' : result
        }), 200    
    
#Metodo POST para insertar usuarios    
@app1.route('/usuarios', methods=["POST"])
def insertUser() :
        
    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "INSERT INTO usuarios(Usu_Id, Usu_Nombre, Usu_Telefono, Usu_Correo) VALUES(%s, %s, %s, %s)"
            cursor.execute(sql, (data['Usu_Id'], data['Usu_Nombre'], data['Usu_Telefono'], data['Usu_Correo']))

            connection.commit()

            return jsonify ({
                'message' : 'Usuario creado exitosamente'
            }), 201

#Metodo PUT para actualizar usuarios        
@app1.route('/usuarios/<int:Usu_Id>', methods=["PUT"])
def updatetUser(Usu_Id) :

    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            try :
                sql = "UPDATE usuarios SET Usu_Nombre = %s, Usu_Telefono = %s WHERE Usu_Id = %s"
                cursor.execute(sql, (data['Usu_Nombre'], data['Usu_Telefono'], Usu_Id))

                connection.commit()

                if cursor.rowcount == 0:
                    return jsonify({"error": "Elemento no encontrado"}), 404

                return jsonify ({ 'message' : 'Usuario actualizado exitosamente'}), 200       
            
            except Exception as e:
                return jsonify({"error": str(e)}), 500
            finally:
                cursor.close()

#Metodo DELETE para eliminar usuarios
@app1.route('/usuarios/<int:Usu_Id>', methods=['DELETE'])
def deleteUser(Usu_Id):
    
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            try:
                sql = "DELETE FROM usuarios WHERE Usu_Id = %s"
                cursor.execute(sql, (Usu_Id,))
                
                connection.commit()
                
                cursor.close()
                
                return jsonify({'mensaje': 'Registro eliminado exitosamente'}), 200
            except Exception as e:
                return jsonify({'error': str(e)}), 500   
             

#if __name__ == '__main__' : 
#    app.run(debug=True)    