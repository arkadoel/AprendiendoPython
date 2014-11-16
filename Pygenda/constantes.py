
class const:
    DB_PATH = "./DB/pygenda.db"

    class sql:
        SELECT = "select * from Persona;"
        SELECT_BY_ID = "select * from Persona where id=?;"
        INSERT = "insert into Persona" \
                 " (Nombre, Apellidos, Fijo, ExtFijo, Movil, ExtMovil, Email, Departamento) " \
                 "values(?,?,?,?,?,?,?,?);"
        UPDATE = """
                    update Persona set
                    Nombre = ?,
                    Apellidos=?,
                    Fijo=?,
                    ExtFijo=?,
                    Movil=?,
                    ExtMovil=?,
                    Email=?,
                    Departamento=?
                    where id = ?;
                  """
        DELETE = """
                    delete from Persona where id =?;
                """
