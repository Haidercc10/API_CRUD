from flask import Blueprint, jsonify, request  
from connectionBD import connection_mysql 

app2 = Blueprint('Companies', __name__)

#Metodo GET para crear empresas
@app2.route('/empresas', methods=['GET'])
def listCompanies() :
    connection = connection_mysql()

    with connection.cursor() as cursor : 

        sql = 'SELECT Emp_Id, Emp_Digito, Emp_Nombre, Emp_Ciudad FROM empresas'
        cursor.execute(sql)

        result = cursor.fetchall()
        return jsonify({
            'data' : result
        }), 200

#Metodo POST para insertar empresas    
@app2.route('/empresas', methods=["POST"])
def insertCompany() :
        
    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "INSERT INTO empresas(Emp_Id, Emp_Digito, Emp_Nombre, Emp_Ciudad) VALUES(%s, %s, %s, %s)"
            cursor.execute(sql, (data['Emp_Id'], data['Emp_Digito'], data['Emp_Nombre'], data['Emp_Ciudad']))

            connection.commit()

            return jsonify ({
                'message' : 'Empresa creada exitosamente'
            }), 201

#Metodo PUT para actualizar empresas        
@app2.route('/empresas/<int:Emp_Id>', methods=["PUT"])
def updatetCompany(Emp_Id) :

    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            try :
                sql = "UPDATE empresas SET Emp_Nombre = %s, Emp_Ciudad = %s WHERE Emp_Id = %s"
                cursor.execute(sql, (data['Emp_Nombre'], data['Emp_Ciudad'], Emp_Id))

                connection.commit()

                if cursor.rowcount == 0:
                    return jsonify({"error": "Elemento no encontrado"}), 404

                return jsonify ({ 'message' : 'Empresa actualizada exitosamente'}), 200       
            
            except Exception as e:
                return jsonify({"error": str(e)}), 500
            finally:
                cursor.close()

#Metodo DELETE para eliminar empresas
@app2.route('/empresas/<int:Emp_Id>', methods=['DELETE'])
def deleteCompany(Emp_Id):
    
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            try:
                sql = "DELETE FROM empresas WHERE Emp_Id = %s"
                cursor.execute(sql, (Emp_Id,))
                
                connection.commit()
                
                cursor.close()
                
                return jsonify({'mensaje': 'Registro eliminado exitosamente'}), 200
            except Exception as e:
                return jsonify({'error': str(e)}), 500          
      

#if __name__ == '__main__' : 
#    app2.run(debug=True)    